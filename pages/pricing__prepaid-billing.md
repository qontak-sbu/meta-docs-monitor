# Prepaid billing



Prepaid billing lets you add funds to a Messaging account before you send messages, and have message charges drawn from that balance. It is an alternative to invoiced billing, where Meta bills you after the fact.

Prepaid billing is available in India, and it is chosen the first time a Messaging account sets up a payment method. Adding funds by UPI puts the account on prepaid billing; saving a card puts it on invoiced billing. Accounts already on invoiced billing are not moved to prepaid billing, and the choice cannot be changed afterwards — see [Availability](#availability).

**Warning:** Not to be confused with the WhatsApp [Payments API](https://developers.facebook.com/documentation/business-messaging/whatsapp/payments/payments-in/upi-intent), which lets your customers pay *you* inside a chat. Prepaid billing is what *you* pay Meta for messaging.

## Availability

| Attribute | Value |
| --- | --- |
| Countries | India |
| Currency | INR |
| Funding method | UPI |
| Account types | Messaging accounts that have not yet set up a payment method |
| Not available for | Meta Business Agent accounts; accounts billed through a Solution Partner&#039;s line of credit; accounts outside India |

## How it works

1. **Add funds.** An admin on the account adds funds to the Messaging account in the [Billing Hub](https://business.facebook.com/billing_hub/accounts/), paying by UPI. The funds appear as Available funds on the account.
2. **Send.** When you call the messages endpoint, WhatsApp checks that the current balance covers the cost of the message plus any charges already incurred but not yet settled, inclusive of applicable taxes. If it does not, the message is rejected. The rejection can reach your integration either as an error on the send call, or as a `messages` status webhook with `status` of `failed` and error code `131042` — so your integration must handle both. When the rejection comes back on the webhook, the send call itself still returns `accepted`. See [Insufficient-funds webhook](#insufficient-funds-webhook). Separately, the admins on the account are notified when the balance is low or empty; those notifications go to people, not to your webhook endpoint. See [Low balance notifications](#low-balance-notifications).
3. **Deliver.** When a message is delivered, its cost is recorded as pending spend and counted in subsequent balance checks. The underlying stored-balance wallet is debited later during settlement.
4. **Settle.** Held charges are settled against the balance on a recurring basis, and appear on your invoices and receipts as usual.

Because the check happens against *pending plus new* charges, the current balance is the amount you can still spend, not the amount you have added.

## Adding funds

Adding funds happens in the [Billing Hub](https://business.facebook.com/billing_hub/accounts/), not through the API. There is no API to add funds to a Messaging account.

## What changes for your integration

For most integrations, nothing. The messages endpoint, message types, templates, and webhooks are unchanged. The one behavior you must handle is rejection for insufficient funds.

### A successful send response does not mean the message was billable

The Cloud API returns HTTP 200 with `message_status` of `accepted` once your send request has been accepted for processing. A funds rejection can also be returned directly on the send call as an error response. When it is not, the send succeeds and a message that is rejected for insufficient funds still returns `accepted` on the send call.

```json
&#123;
  &quot;messaging_product&quot;: &quot;whatsapp&quot;,
  &quot;contacts&quot;: [&#123; &quot;input&quot;: &quot;919xxxxxxxxx&quot;, &quot;wa_id&quot;: &quot;919xxxxxxxxx&quot; &#125;],
  &quot;messages&quot;: [&#123; &quot;id&quot;: &quot;wamid.HBgM...&quot;, &quot;message_status&quot;: &quot;accepted&quot; &#125;]
&#125;
```

The rejection is often delivered on the [status webhook](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) rather than on the send call. If your app is not subscribed to webhooks, you will not see those, and the message will simply never reach the `sent` status.

**Warning:** Subscribe to the `messages` webhook field before sending on a prepaid account. Treat `accepted` as &quot;queued&quot;, not as &quot;will be delivered&quot;. This is true of all accounts, but on a prepaid account an app that is not subscribed can miss a funds rejection entirely. Handle error responses on the send call as well.

### Insufficient-funds webhook

When a rejection for insufficient funds is reported on the webhook, it arrives as a `messages` status webhook with `status` of `failed`. `error_data.details`, `title`, and `message` contain generic payment-eligibility text. Do not use them to determine whether Available funds were insufficient. `href` links to the page you should act on.

```json
&#123;
  &quot;object&quot;: &quot;whatsapp_business_account&quot;,
  &quot;entry&quot;: [&#123;
    &quot;id&quot;: &quot;WHATSAPP_BUSINESS_ACCOUNT_ID&quot;,
    &quot;changes&quot;: [&#123;
      &quot;field&quot;: &quot;messages&quot;,
      &quot;value&quot;: &#123;
        &quot;messaging_product&quot;: &quot;whatsapp&quot;,
        &quot;metadata&quot;: &#123; &quot;display_phone_number&quot;: &quot;...&quot;, &quot;phone_number_id&quot;: &quot;...&quot; &#125;,
        &quot;statuses&quot;: [&#123;
          &quot;id&quot;: &quot;wamid.HBgM...&quot;,
          &quot;status&quot;: &quot;failed&quot;,
          &quot;timestamp&quot;: &quot;1755600000&quot;,
          &quot;recipient_id&quot;: &quot;919xxxxxxxxx&quot;,
          &quot;errors&quot;: [&#123;
            &quot;code&quot;: 131042,
            &quot;title&quot;: &quot;Business eligibility payment issue&quot;,
            &quot;message&quot;: &quot;Business eligibility payment issue&quot;,
            &quot;error_data&quot;: &#123;
              &quot;details&quot;: &quot;Message failed to send because there were one or more errors related to your payment method.&quot;
            &#125;,
            &quot;href&quot;: &quot;https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes/&quot;
          &#125;]
        &#125;]
      &#125;
    &#125;]
  &#125;]
&#125;
```

| Code | Title | Meaning on a prepaid account | What to do |
| --- | --- | --- | --- |
| `131042` | Business eligibility payment issue | The message failed a payment-eligibility check. An insufficient current balance is one possible cause. | Check the current balance and payment eligibility. Add funds only if the current balance is insufficient. |

The message is normally not delivered or charged. Confirm its final status before resending. If the balance was insufficient, add funds and wait until they are available.

Do not parse `error_data.details` to detect a funds problem. On a prepaid account the text refers to your payment method, not to your balance, and it reads the same whether the account has no payment method, an invalid one, or simply an insufficient current balance. Treat `131042` as &quot;payment eligibility failed&quot;, and check the current balance separately.

On Graph API versions before v16, this text is returned in `title` instead of in `error_data.details`.

### A second rejection: rate limit

A send can also fail with error `130429`, a rate-limit response. It arrives on the same status webhook with a different code.

| Code | Title | Meaning on a prepaid account | What to do |
| --- | --- | --- | --- |
| `130429` | Rate limit hit | The send was rate-limited. This code alone does not show whether the current balance is sufficient. | Slow sending and retry. Check the current balance separately; add funds only if it is insufficient. |

Handle `130429` as a rate-limit response. Slow sending and retry. If it continues, check the current balance and escalate.

### Recommended handling

- **Subscribe to `messages` webhooks** and inspect the error details. `131042` is a payment-eligibility failure, not proof that the current balance is insufficient.
- **Do not retry immediately in a tight loop.** Back off, or pause the queue for that account, and surface the condition to whoever administers the account.
- **Pause bulk sends if payment-eligibility failures repeat.** Check the current balance and payment eligibility before resuming.
- **Reconcile against delivery, not acceptance.** Use `sent` and `delivered` statuses as your record of what was billable.
- Use the error details and current account state to decide whether to add funds, slow sending, or escalate.

## Checking the balance

The current balance is shown on the account in the [Billing Hub](https://business.facebook.com/billing_hub/accounts/), on the Balance card, where it is labelled **Available funds**.

There is no public API for reading the current balance. If your integration receives `131042`, ask an admin on the account to check the current balance and payment eligibility before retrying.

## Low balance notifications

Admins on an account using prepaid billing receive notifications when the account balance is low, and when it reaches zero. These are delivered by email, in the Meta Business Suite notification jewel, and as a banner in WhatsApp Manager; they are not delivered to your webhook endpoint.

## Taxes

Charges are inclusive of applicable Indian taxes (GST). The funds check reserves enough balance to cover tax on your outstanding charges as well as on the message being sent, so the current balance required to send a message is higher than the message&#039;s list rate.

Invoices show the tax breakdown. See [Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing) for the underlying per-message rates.

## Limitations

- Funds can be added only through the [Billing Hub](https://business.facebook.com/billing_hub/accounts/). There is no add-funds API.
- An account cannot move between prepaid and invoiced billing. The payment method is fixed once set; using a different one requires creating a new Messaging account.
- The current balance cannot be read through the API.
- Prepaid funds cannot be shared across Messaging accounts.
- Funds are held in INR and cannot be converted to another currency.

## Troubleshooting

**My send returned 200 and `accepted`, but the message never arrived.**

Check your `messages` status webhook for a `failed` status and inspect its error details. Error `131042` is a payment-eligibility failure; an insufficient current balance is one possible cause. If you are not receiving webhooks, publish your app, then use the [Subscribed Apps API](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-account/subscribed-apps-api) to [subscribe your app to webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-account/subscribed-apps-api#post-version-waba-id-subscribed-apps) with a configured callback URL. Without a subscription, the rejection has nowhere to be delivered. See [Webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/overview).

**I added funds but sends still fail with `131042`.**

Check the current balance in the Billing Hub. The check includes charges already incurred but not yet settled, plus tax, not just the new message. If the current balance is sufficient and `131042` persists, verify payment eligibility and escalate.

**Sends started failing partway through a batch.**

If the failures indicate insufficient funds, the current balance may have run out mid-batch. Messages already delivered are charged; failed messages are not. Add funds, wait until they are available, then resend the failed messages.

## See also

- [Pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
- [Status messages webhook reference](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status)
- [Cloud API error codes](https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes)


---

Full documentation index for this product: https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt
