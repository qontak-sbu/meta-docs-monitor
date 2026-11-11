#!/usr/bin/env python3
"""Meta Docs Monitor - daily downloader.

Downloads the raw markdown (.md) of every watched Meta WhatsApp docs page,
saves it under pages/, and writes reports/status.json describing what was
fetched. The GitHub workflow then commits the files and stores the exact
line-by-line diff in reports/latest.diff.

A page that fails to download keeps its previous file, so a failure never
shows up as "content removed".
"""
import hashlib
import json
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(ROOT, "pages")
REPORTS_DIR = os.path.join(ROOT, "reports")
STATUS_FILE = os.path.join(REPORTS_DIR, "status.json")
RULES_FILE = os.path.join(ROOT, "rules.txt")

WA_BASE = "https://developers.facebook.com/documentation/business-messaging/whatsapp/"
USER_AGENT = "meta-docs-monitor/1.0 (GitHub Actions; daily check of public docs)"
RETRY_WAITS = [5, 20, 60]  # seconds to wait before each retry
WIB = timezone(timedelta(hours=7))


def load_rules():
    """Rule URLs (no .md). Each rule covers the page itself plus its children."""
    rules = []
    with open(RULES_FILE, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                rules.append(line.rstrip("/").removesuffix(".md"))
    return rules


def index_url_for(rule):
    """Meta keeps separate llms.txt indexes for /reference/ and /flows/."""
    for folder in ("reference/", "flows/"):
        if rule.startswith(WA_BASE + folder):
            return WA_BASE + folder + "llms.txt"
    return WA_BASE + "llms.txt"


def fetch(url):
    """Return (http_status, text, error). Retries on any failure."""
    last_status, last_error = None, None
    for attempt in range(len(RETRY_WAITS) + 1):
        if attempt:
            time.sleep(RETRY_WAITS[attempt - 1])
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read().decode("utf-8", errors="replace")
                last_status = resp.status
                ctype = resp.headers.get("Content-Type", "")
            if not body.strip():
                last_error = "empty response"
                continue
            if "html" in ctype.lower() or body.lstrip()[:15].lower().startswith(("<!doctype", "<html")):
                last_error = f"got an HTML page instead of markdown ({ctype})"
                continue
            return last_status, body, None
        except urllib.error.HTTPError as e:
            last_status, last_error = e.code, f"HTTP {e.code}"
        except Exception as e:  # network errors, timeouts
            last_error = f"{type(e).__name__}: {e}"
    return last_status, None, last_error


def slug(page_url):
    """pricing/ai-providers -> pricing__ai-providers.md"""
    path = page_url.removeprefix(WA_BASE).strip("/")
    return path.replace("/", "__") + ".md"


def headings(text):
    return [ln.strip() for ln in text.splitlines() if re.match(r"^#{1,6} ", ln)]


def updated_date(text):
    m = re.search(r"Updated:?\s*([A-Z][a-z]{2,8}\.? \d{1,2}, \d{4})", text)
    return m.group(1) if m else None


def sha256(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    os.makedirs(PAGES_DIR, exist_ok=True)
    os.makedirs(os.path.join(REPORTS_DIR, "history"), exist_ok=True)

    previous = {}
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, encoding="utf-8") as f:
            previous = json.load(f)
    prev_pages = {p["url"]: p for p in previous.get("pages", [])}
    baseline = not previous

    rules = load_rules()

    # 1. Resolve pages from the index (fall back to last run's list if it fails).
    index_results, pages = {}, {}
    for rule in rules:
        pages[rule] = rule
        idx = index_url_for(rule)
        if idx not in index_results:
            status, text, err = fetch(idx)
            urls = []
            if text:
                found = re.findall(r"https://developers\.facebook\.com/documentation/[^\s)\]>\"']+?\.md", text)
                urls = sorted({u.removesuffix(".md") for u in found})
            index_results[idx] = {"ok": text is not None, "http_status": status,
                                  "error": err, "chars": len(text) if text else 0, "urls": urls}
        res = index_results[idx]
        if res["ok"]:
            for u in res["urls"]:
                if u.startswith(rule + "/"):
                    pages[u] = rule
        else:
            for u, p in prev_pages.items():
                if p.get("rule") == rule:
                    pages[u] = rule

    # Pages tracked before but no longer listed in a working index.
    removed = []
    for u, p in prev_pages.items():
        if u in pages:
            continue
        idx = index_url_for(p.get("rule", u))
        if index_results.get(idx, {}).get("ok"):
            removed.append(u)

    # 2. Download every page.
    results = []
    for url in sorted(pages):
        file_name = slug(url)
        path = os.path.join(PAGES_DIR, file_name)
        old_text = open(path, encoding="utf-8").read() if os.path.exists(path) else None
        status, text, err = fetch(url + ".md")
        entry = {"url": url, "rule": pages[url], "file": "pages/" + file_name,
                 "http_status": status, "ok": text is not None, "error": err,
                 "new_page": old_text is None and url not in prev_pages and not baseline}
        if text is not None:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            entry.update({"chars": len(text), "sha256": sha256(text),
                          "sections": len(headings(text)), "updated_date": updated_date(text),
                          "changed": old_text is not None and sha256(old_text) != sha256(text)})
            if old_text is not None:
                entry["previous_chars"] = len(old_text)
                entry["previous_updated_date"] = updated_date(old_text)
        else:
            entry.update({"changed": False, "note": "download failed; previous file kept unchanged"})
        results.append(entry)

    now = datetime.now(timezone.utc)
    report = {
        "run_utc": now.strftime("%Y-%m-%d %H:%M"),
        "run_wib": now.astimezone(WIB).strftime("%Y-%m-%d %H:%M"),
        "baseline": baseline,
        "rules": rules,
        "indexes": {k: {kk: vv for kk, vv in v.items() if kk != "urls"} | {"pages_found": len(v["urls"])}
                    for k, v in index_results.items()},
        "pages_checked": len(results),
        "pages_failed": sum(1 for r in results if not r["ok"]),
        "pages_changed": sum(1 for r in results if r.get("changed")),
        "pages_new": sum(1 for r in results if r.get("new_page")),
        "removed_pages": removed,
        "pages": results,
    }
    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Checked {report['pages_checked']} pages: {report['pages_changed']} changed, "
          f"{report['pages_failed']} failed, {report['pages_new']} new, {len(removed)} removed.")
    for r in results:
        print(f"  {'OK ' if r['ok'] else 'ERR'} {r['url']} {r.get('chars', '')} {r.get('error') or ''}")


if __name__ == "__main__":
    main()
