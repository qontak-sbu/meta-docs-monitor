# Pricing on the WhatsApp Business Platform


**Warning:** This page encompasses pricing across Cloud API and the Marketing Messages API for WhatsApp, for the following message categories: Marketing, utility, authentication, service, and Meta Business Agent.

**Warning:** This page reflects pricing updates that became effective as of October 1, 2026 by Messaging account timezone. Full detail on these updates is [below](#effective-october-1-2026).

## How Meta charges for messages &#123;#how-meta-charges-for-messages&#125;

Effective July 1, 2025 – Meta charges on a **per-message basis**, aligned to industry standards. Meta charges by category–market, and only for messages from businesses to users. Meta does **not** charge for messages from users to businesses.

- Businesses are only charged when a message is _delivered_. Meta does _not_ charge for messages sent.
- Rates for messages vary based on 2 factors: a. the message [category](#message-categories) (“category”) and b. the recipient WhatsApp phone number’s [country calling code](#pricing-regions-on-the-rate-card-country-calling-codes) (“market”).

### Message categories &#123;#message-categories&#125;

Meta has 5 different message categories on the WhatsApp Business Platform, with the introduction of Meta Business Agent as of July 1, 2026. A message from a business to a user only has 1 of the 5 categories and thus can only incur up to 1 charge, per the message’s category.

#### Template messages &#123;#template-messages&#125;

_Businesses can use template messages to reach out to users_ – **Template messages** (`&quot;type&quot;:&quot;template&quot;`) can be delivered at any time. Template messages are categorized into 3 categories, per below; see [template categorization](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization) to learn how template message categorization works.

1. **Marketing** – template messages for promotional objectives
2. **Utility** – template messages for transactional or informational objectives
3. **Authentication** – template messages for identity verification objectives

#### Non-template messages &#123;#non-template-messages&#125;

_Businesses can use non-template messages only to respond to users_ – **Non-template messages** (`&quot;type&quot;:&quot;text&quot;`, `&quot;type&quot;:&quot;image&quot;`, and so on) can only be sent in an open 24-hour [customer service window](#customer-service-window-csw), which opens and resets with each user message. Note that a business can also choose to use template messages to respond to users; however, non-template messages _cannot_ be used to reach out to users.

1. **Service** – Any non-template message _not_ powered by the Meta Business Agent Platform. These can be powered by a 3rd-party AI solution or people (like customer service representatives). Message types (outlined in [Send messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#message-types)) include address messages, audio messages, interactive location request messages, and more.
2. **Meta Business Agent** – Any non-template message powered by the Meta Business Agent Platform.

### Charges by message category &#123;#charges-by-message-category&#125;

#### Charges for marketing, utility, authentication and service messages &#123;#charges-for-marketing-utility-authentication-and-service-messages&#125;

- _Charge for_: Delivered message.
- _Meter_: Per message.
- _Rate_: Varies by market, aligned to industry standards. Rates by category vary as well, thus rates vary by market–category.
- _Cost per message_:
    - Utility, authentication, and service: Fixed, per published rates.
    - Marketing: For Cloud API, fixed, per published rates. For Marketing Messages API for WhatsApp, can vary per message if businesses choose to use the [max price feature](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/pricing).
- _Volume tiers_: For utility and authentication messages only. Learn more about [volume tiers](#volume-tiers-for-utility-and-authentication-messages).
- _Frequency of updates_: Per published pricing calendar.
- _Free messages_: Two instances (all messages in free entry point window; free tier of monthly service messages). Learn more about [when Meta does not charge](#when-meta-does-not-charge).

#### Charges for Meta Business Agent messages &#123;#charges-for-meta-business-agent-messages&#125;

- _Charge for_: Delivered message.
- _Meter_: Per message, based on one per-token charge that encompasses AI agent processing (token consumption) and message delivery. Meta only charges for input and output tokens and does _not_ charge for cache tokens.
- _Rate_: One global rate of $2.00 USD per 1 million (M) tokens. One message typically consumes 20,000–25,000 tokens, which translates to approximately 4–5 cents (USD) per message.
- _Cost per message_: Varies with complexity. Simple responses consume fewer tokens and cost less; complex responses consume more tokens and cost more.
- _Volume tiers_: Do not apply.
- _Free messages_: Do not apply.

### Pricing example &#123;#example-across-all-message-categories&#125;

Below is an example of an interaction between a business and a user. It starts with the business reaching out with a marketing template; using Meta Business Agent to respond to user questions; triggering an escalation to a customer service representative; and ultimately sending an order confirmation, all within one hour. Things to note:

- Meta charges for each message from the business to the user. Since there are 5 delivered messages, there are 5 charges.
- Every message has only one charge, per the category of that message. The “message category” and “charges incurred” columns always align.
- If this had all started with a user messaging a business from an Ad that Clicks to WhatsApp – thus happening in a [free entry point window](#free-entry-point-window-fep) – 3 of the 5 messages would _not_ be charged. Meta Business Agent remains charged.

| **Message content** | **Sender** | **Message type** | **Message category** | **Charges incurred** |
| Cart abandonment reminder | Business | Template | Marketing | Marketing |
| “Do you have this in a size Small?” | User | – | – | – |
| Meta-powered response to user’s question | Business | Non-template | Meta Business Agent | Meta Business Agent |
| “Do you have this in white?” | User | – | – | – |
| Meta-powered response to user’s question | Business | Non-template | Meta Business Agent | Meta Business Agent |
| “I’m ready to check-out, but my card is expired” | User | – | – | – |
| _Meta Business Agent hands off to customer service representative_ | _Meta Business Agent hands off to customer service representative_ | _Meta Business Agent hands off to customer service representative_ | _Meta Business Agent hands off to customer service representative_ | – |
| Customer service rep responds to user’s question | Business | Non-template | Service | Service |
| Order confirmation | Business | Template | Utility | Utility |
|  |  |  | **Total charges** | **5 charges** |

### Markets &#123;#markets&#125;

As of October 1, 2026 – Meta has 47 markets on its rate card. 39 of these represent named countries (like Brazil, Mexico, India) and 8 of these represent regions (like Rest of Latin America). A mapping of these with phone number country calling codes is [below](#pricing-regions-on-the-rate-card-country-calling-codes). If a business delivers a message to a user in a country that is…

- Named on the rate card → Meta charges that market’s rate
- In a “Rest of” region → Meta charges that region’s rate, across all markets within that region

## What Meta charges for messages &#123;#what-meta-charges-for-messages&#125;

Meta publishes rates for transparency, across all 5 categories x 47 markets. See our [rate cards and volume tiers](#rate-cards-and-volume-tiers).

### Rate cards and volume tiers &#123;#rate-cards-and-volume-tiers&#125;

Rate cards below reflect our current rates and volume tiers, effective October 1, 2026, based on your Messaging account timezone. Rates are also available interactively on our [WhatsApp Business website](https://business.whatsapp.com/products/platform-pricing#rates).

| Currency | Launched in 2026? | **List rates** (CSV) | **Volume tiers for utility and authentication** (CSV) | **List rates and volume tiers** (PDF) |
| --- | --- | --- | --- | --- |
| USD | Available already | USD list rates | USD volume tiers | USD rates and volume tiers |
| AED | April 1, 2026 | AED list rates | AED volume tiers | AED rates and volume tiers |
| ARS | April 1, 2026 | ARS list rates | ARS volume tiers | ARS rates and volume tiers |
| AUD | Available already | AUD list rates | AUD volume tiers | AUD rates and volume tiers |
| BRL | July 1, 2026 | BRL list rates | BRL volume tiers | BRL rates and volume tiers |
| CLP | April 1, 2026 | CLP list rates | CLP volume tiers | CLP rates and volume tiers |
| COP | April 1, 2026 | COP list rates | COP volume tiers | COP rates and volume tiers |
| EUR | Available already | EUR list rates | EUR volume tiers | EUR rates and volume tiers |
| GBP | Available already | GBP list rates | GBP volume tiers | GBP rates and volume tiers |
| IDR | Available already | IDR list rates | IDR volume tiers | IDR rates and volume tiers |
| INR | Available already | INR list rates | INR volume tiers | INR rates and volume tiers |
| MXN | January 1, 2026 | MXN list rates | MXN volume tiers | MXN rates and volume tiers |
| MYR | April 1, 2026 | MYR list rates | MYR volume tiers | MYR rates and volume tiers |
| PEN | April 1, 2026 | PEN list rates | PEN volume tiers | PEN rates and volume tiers |
| SAR | April 1, 2026 | SAR list rates | SAR volume tiers | SAR rates and volume tiers |
| SGD | April 1, 2026 | SGD list rates | SGD volume tiers | SGD rates and volume tiers |

### Currencies &#123;#currencies&#125;

As of July 1, 2026 – Meta has 16 currencies enabled on the WhatsApp Business Platform, after having introduced +10 currencies in 2026, as outlined in the table above. Currency selection is part of the Messaging account creation process; once selected, a currency cannot be changed. Businesses can leverage our [Currency Migration APIs](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/change-billing-currency) to more easily choose a different currency.

### Comparing Meta Business Agent to service messages &#123;#comparing-meta-business-agent-to-service-messages&#125;

Below is a side-by-side comparison of the expected cost to send 10,000 AI-powered messages in response to users in Brazil via high-complexity AI models vs. Meta Business Agent. Estimates for 3rd-party AI solutions are based on publicly-available information and benchmarks.

| Message category | Service | Meta Business Agent |
| --- | --- | --- |
| **AI agent performance** | Higher-complexity | Higher-complexity |
| **AI agent cost** | **~9 ¢** per message&lt;br&gt;(estimate of 3rd-party cost) | **~4-5 ¢** per message&lt;br&gt;$2.00/1M tokens&lt;br&gt;x ~25k tokens&lt;br&gt;(estimate) |
| **Message delivery**1 | **0.68 ¢** per message1 | **~4-5 ¢** per message&lt;br&gt;$2.00/1M tokens&lt;br&gt;x ~25k tokens&lt;br&gt;(estimate) |
| **Total** | **~9-10 ¢** per message | **~4-5 ¢** per message |
| **Total for 10k messages** | **~ $968** | **~ $400 - $500** |
| 1 Based on Meta’s [current rate](#rate-cards-and-volume-tiers) for utility and authentication messages to users in Brazil. | 1 Based on Meta’s [current rate](#rate-cards-and-volume-tiers) for utility and authentication messages to users in Brazil. | 1 Based on Meta’s [current rate](#rate-cards-and-volume-tiers) for utility and authentication messages to users in Brazil. |

Also, price per-message for Meta Business Agent can vary by complexity, aligned to industry norms. The following table shows example interactions powered by Meta Business Agent and their estimated cost.

| **Type of interaction** | **Example user message** | **# messages to the user in the interaction** | **Tokens consumed** | **Est. Meta Business Agent cost** |
| _Simple inquiry_ | “At what time do you open?” | 4 | ~80k → ~20k/mssg | ~ 16-20 ¢ |
| _Complex interaction_ | &quot;I&#039;m stuck on step 3 of this assembly — can you walk me through it?&quot; | 10 | ~250k → ~25k/mssg | ~ 40 - 50 ¢ |

## When Meta may update pricing &#123;#when-meta-may-update-pricing&#125;

### Pricing calendar &#123;#pricing-calendar&#125;

As of September 2025, Meta has published a pricing calendar to provide clear, go-forward guidance to better enable businesses to plan and prepare for pricing updates:

- Meta may update pricing only on the 1st day of each quarter, thus up to 4 times per year: January 1, April 1, July 1, and/or October 1.
- Meta will provide advanced notice that is better aligned to the effort required to implement different types of pricing updates, per below:

| **Type of pricing update** | **Examples** | **Minimum advanced notice** |
| **Rate card update** | Updating the rate for a given market–category&lt;br&gt;Updating the volume tiers for a given market–category (utility and authentication only)&lt;br&gt;Moving a market from one [pricing region](#pricing-regions-on-the-rate-card-country-calling-codes) (for example, “Other”) to another OR to be standalone on the rate card | 1 month |
| **Pricing model add-on** | Our July 1, 2025, introduction of new [volume tiers](#volume-tiers-for-utility-and-authentication-messages) for utility and authentication messages | 3 months |
| **Pricing model change** | Our July 1, 2025 update to our pricing model, from conversation-based pricing to per-message pricing | 6 months |

## When Meta does _not_ charge &#123;#when-meta-does-not-charge&#125;

There are two instances where Meta does _not_ charge for a message a business delivers to a WhatsApp user:

- _In the_ [free entry point window](#free-entry-point-window-fep) – In this window, Meta does _not_ charge for marketing, utility, authentication or service messages. Meta Business Agent messages remain charged.
- _For the_ [first 1,000 service messages each month](#free-tier-of-monthly-service-messages) – For each business phone number, Meta provides 1,000 free service messages per month, which do not roll over but reset monthly. Thus, Meta only charges as of the 1,001st service message for each business phone number.

Also, as noted above, Meta does not charge for messages from a WhatsApp user to a business.

## Ways Meta provides value via pricing &#123;#ways-meta-provides-value-via-pricing&#125;

### Free entry point window (FEP) &#123;#free-entry-point-window-fep&#125;

If a WhatsApp user messages you via an ad that clicks to WhatsApp (CTWA) using a device running our Android or iOS app (since our desktop and web apps are not supported):

1. A [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows) is opened.
2. If you respond within the [customer service window](#customer-service-window-csw) with a marketing, utility, authentication or service message:
    - That message is _not_ charged and opens a Free Entry Point (“FEP”) window, starting from the time when you responded.
    - The FEP window may remain open for up to 7 days.
    - While open, Meta does _not_ charge for marketing, utility, authentication or service messages. Meta continues to charge for Meta Business Agent messages in the FEP window.

In the example below, all messages from the business to the user are _not_ charged because they opened or were in the FEP window.

| **Message content** | **Sender** | **Message type** | **Message category** | **Charges incurred** |
| User messages from a CTWA ad:&lt;br&gt;“Do you have this in white?” | User | – | – | – |
| [Interactive media carousel message](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/interactive-media-carousel-messages/) to showcase available colors for that product | Business | Template | Marketing | _No charge_&lt;br&gt;_Opens FEP window_ |
| “Do you have this in size small?” | User | – | – | – |
| Customer service rep responds to user’s question | Business | Non-template | Service | _No charge_ in open FEP window |
| Order confirmation | Business | Template | Utility | _No charge in open FEP window_ |
|  |  |  | **Total charges** | **0 charges** |

#### Free entry point windows with multiple Messaging accounts &#123;#free-entry-point-windows-with-multiple-messaging-accounts&#125;

Like customer service windows, a free entry point window is tracked for the business and WhatsApp user pair, not for an individual Messaging account. When several Messaging accounts send on the same business phone number, they all share the same FEP window:

- Any Messaging account sending on that phone number can send free messages while the FEP window is open.
- The Messaging account that funded the Click to WhatsApp ad does not get exclusive use of the window.
- If a different Messaging account responds to the WhatsApp user than the one that funded the ad, messages are still free while the window is open.

### Free tier of monthly service messages &#123;#free-tier-of-monthly-service-messages&#125;

**Warning:** This only applies to service messages, as of 12am by Messaging account timezone on October 1, 2026.

As Meta resumes charging for service messages, Meta provides every business phone number with a free tier of 1,000 service messages per month.

- Each business phone number has one free tier of 1,000 delivered service messages per month. Meta charges as of the 1,001st service message per month, after the free tier has been used.
- Unused service messages in the free tier do not roll over to the next month. The free tier resets monthly for each business phone number (for example, 1,000 for October with no roll-over; 1,000 for November with no roll-over). This reset happens at 12am by Messaging account timezone.
- If businesses do not have a payment method for their Messaging account(s), Meta will deliver service messages within the free tier but _not_ deliver them after the free tier has been used. To ensure continuity of service messages as of October 1, 2026, please ensure you have a payment method in [Billing Hub](https://business.facebook.com/latest/billing_hub/).

When Meta begins to charge – as of the 1,001st service message each month – the pricing type (`&lt;PRICING_TYPE&gt;`) in the pricing object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks for messages with a pricing category (`&lt;PRICING_CATEGORY&gt;`) of service will change from `free_customer_service` to `regular` as outlined below:

| Which service messages | Through Sep. 30, 2026 | Through Sep. 30, 2026 | As of Oct. 1, 2026 | As of Oct. 1, 2026 | `type` | Charged | `type` | Charged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Service messages in the free tier, per business phone number | `free_customer_service` | **No** | `free_customer_service` | **No** |
| Service messages after the free tier has been used, per business phone number | `free_customer_service` | **No** | `regular` | **Yes** |

**Service message in the free monthly tier** – For a service message delivered while the business phone number is within its free tier:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_customer_service&quot;,
  &quot;category&quot;: &quot;service&quot;
&#125;
```

**Service message that is charged** – For a service message delivered _after_ the business phone number’s free tier has been used:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;service&quot;
&#125;
```

### Volume tiers for utility and authentication messages &#123;#volume-tiers-for-utility-and-authentication-messages&#125;

**Warning:** Volume tiers only apply to utility and authentication messages.

Businesses can unlock lower utility and authentication rates based on the number of messages they send in a month, by market–category.

#### Tiering accrual &#123;#tiering-accrual&#125;

- Messages are aggregated at the business portfolio level, across all Messaging accounts owned by the portfolio — To determine what tier rates may apply in a given month for a given market–category pair, Meta aggregates messages across all of a business portfolio&#039;s Messaging accounts for each market-category pair (for example, Brazil–authentication, Brazil–utility, India–authentication, and so on).
- Only messages that are charged count toward the tiers. Thus, any utility or authentication messages sent in a free entry point window do _not_ count toward volume tiers.
- Volume tiers will be determined solely by Meta — All insights data is approximate due to small variations in data processing. Undue reliance should not be placed on insights data.

#### How volume tiers work &#123;#how-volume-tiers-work&#125;

- Tiers are market–category specific — Volume tiers are aligned to our rate cards and differ by market (for example, Brazil or Rest of Latin America) and category (utility, authentication).
- Rates are tier-specific — When a business sends enough messages at a given market–category pair to reach the next tier, they unlock the rate of the next tier, specifically for messages in that tier. This rate applies across all of their Messaging accounts.
- Tiers reset monthly — At the start of the next month (12am Messaging account timezone), message count resets to 0 and businesses begin to accrue messages toward that month.

#### Volume tier examples &#123;#volume-tier-examples&#125;

The table below is illustrative and only highlights the dynamics of volume tiers. Please refer to our [rate cards](#rate-cards-and-volume-tiers) to see the rates charged.

| **India x Authentication messages** (specific market x message category) | **India x Authentication messages** (specific market x message category) | **India x Authentication messages** (specific market x message category) | **India x Authentication messages** (specific market x message category) | **India x Authentication messages** (specific market x message category) |
| **Messages per month** | **Messages per month** | **What Meta charges** (illustrative) | **What Meta charges** (illustrative) | **How it works** |
| **From** | **To** | **Rate** | **vs. List rate** | **How it works** |
| 0 | A | List rate | 0% | First A messages are charged list rate |
| A + 1 | B | Tier rate 1 | – 5% | Only messages A+1 to B are charged tier Rate 1 |
| B + 1 | C | Tier rate 2 | – 10% | Only messages B+1 to C are charged tier Rate 2 |
| C + 1 | ∞ | Tier rate 3 | – 15% | Only messages C+1 onward are charged tier rate 3 |

Below are several examples to highlight how the tiers work and what is charged in a given month, for a given market–category. These examples refer to the illustrative table above:

- _Example 1: A business that sends a total of B authentication messages in a month to India is charged:_
    - List rate for the first A messages.
    - Tier rate 1 for messages A+1 to B.
    - Total charges for that month = Rate per tier 𝗑 messages in each tier.
- _Example 2: A business that starts to be charged our authentication-international rates on the 15th day of the month:_
    - Day 1 to 14 of that month: Volume tiers apply on the authentication rate.
    - Day 15 onward of that month: Volume tiers apply on the authentication-international rate, with messages continuing to accrue in that month. For example, if a business has already reached the Tier 2, the business would be charged Tier 2’s authentication-international rate.

- _Example 3: A business has 3 Messaging accounts sending authentication messages to India. For Messaging account A, it is still July 31 based on their timezone. For Messaging accounts B and C, it is already August 1 based on their timezone. For July, the business is already being charged Tier Rate 1._
    - The business portfolio will be accruing toward tiers for both July (via Messaging account A) and August (via Messaging accounts B, C) for a period of time.
    - The business can reach the next tier for July, via Messaging account A. If that happens, messages for the remainder of July for Messaging account A will be charged Tier Rate 2.
- _Example 4: A business has 3 Messaging accounts, integrated across 2 partners. Provider 1 sends the first B messages in a given month, and provider 2 starts sending messages as of when the business is in the 3rd tier. The business does not send enough messages that month to reach the next tier. What Meta charges each provider:_
    - Provider 1: List rate for A messages, then Tier Rate 1 from A+1 to B, and Tier Rate 2 for B+1 to C.
    - Provider 2: Tier Rate 2 across all of their messages.

#### Tiering webhooks &#123;#tiering-webhooks&#125;

Starting October 1, 2025, an [`account_update`](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/account_update) webhook with `event` set to `VOLUME_BASED_PRICING_TIER_UPDATE` will be triggered when your Messaging account reaches a new volume tier, in any market, in a given month. This complements our [`pricing_analytics`](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics) endpoint, which will continue to provide intra-month tiering progress and tiering information for delivered messages.

Example webhook:

```json
&#123;
  &quot;object&quot;: &quot;whatsapp_business_account&quot;,
  &quot;entry&quot;: [
    &#123;
      &quot;id&quot;: &quot;102290129340398&quot;,
      &quot;time&quot;: 1743451903,
      &quot;changes&quot;: [
        &#123;
          &quot;value&quot;: &#123;
            &quot;volume_tier_info&quot;: &#123;
              &quot;tier_update_time&quot;: 1743451903,
              &quot;pricing_category&quot;: &quot;UTILITY&quot;,
              &quot;tier&quot;: &quot;25000001:50000000&quot;,
              &quot;effective_month&quot;: &quot;2025-11&quot;,
              &quot;region&quot;: &quot;India&quot;
            &#125;,
            &quot;event&quot;: &quot;VOLUME_BASED_PRICING_TIER_UPDATE&quot;
          &#125;,
          &quot;field&quot;: &quot;account_update&quot;
        &#125;
      ]
    &#125;
  ]
&#125;
```

- `tier_update_time` tells when your Messaging account reached a higher volume tier (Unix timestamp).
- `pricing_category` tells you the template category (`UTILITY` or `AUTHENTICATION`) for which your new volume tier rate applies.
- `tier` tells you the new volume tier&#039;s lower and upper bounds.
- `effective_month` tells you the month in which your new volume tier rate is in effect.
- `region` tells you the WhatsApp user country/region for which your new volume tier rate applies.

Note it’s possible for multiple [`account_update`](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/account_update) webhooks to be triggered that describe the same tier switch event. In these cases, use the webhook with the smaller `tier_update_time` Unix timestamp as the official webhook.

#### Tiering analytics &#123;#tiering-analytics&#125;

You can get [volume tier information](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#volume-tier-information) via [pricing analytics](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics).

## Other pricing mechanics &#123;#other-pricing-mechanics&#125;

### Customer service window (CSW) &#123;#customer-service-window-csw&#125;

When a WhatsApp user messages you or [calls you](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/pricing#how-calling-changes-the-24-hour-customer-service-window), a 24-hour timer called a _customer service window_ starts. If the user messages or calls you again before the timer expires, the timer resets to 24 hours. Businesses can only send non-template messages to users when this window is open. If it is not open, businesses can only send template messages to reach out to users.

As a reminder, you can only send messages to WhatsApp users who have opted in to receiving messages from you. Learn more about [customer service windows](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows).

### Authentication-international rates &#123;#authentication-international-rates&#125;

Specific markets have an authentication-international rate. Our [rate cards](#rate-cards-and-volume-tiers) reflect these rates, for the markets where they apply. See [Authentication-International rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates) to learn about these rates and if they apply to your business.

### Pricing regions on the rate card (country calling codes) &#123;#pricing-regions-on-the-rate-card-country-calling-codes&#125;

Charges by message category vary based on the recipient WhatsApp phone number’s country calling code (“market”). The table below shows how Meta maps country calling codes and ISO 3166 Alpha-2 country codes to countries or regions. If a country is not listed below, it maps to Other.

- **Standalone on rate cards** – 39 markets
    - Argentina (AR) - 54
    - Bangladesh (BD) - 880
    - Brazil (BR) - 55
    - Chile (CL) - 56
    - Colombia (CO) - 57
    - Egypt (EG) - 20
    - France (FR) - 33
    - Germany (DE) - 49
    - Hong Kong (HK) - 852
    - Hungary (HU) - 36
    - India (IN) - 91
    - Indonesia (ID) - 62
    - Israel (IL) - 972
    - Iraq (IQ) - 964
    - Italy (IT) - 39
    - Kazakhstan (KZ) - 7
    - Kuwait (KW) - 965
    - Malaysia (MY) - 60
    - Mexico (MX) - 52
    - Morocco (MA) - 212
    - Nepal (NP) - 977
    - Netherlands (NL) - 31
    - Nigeria (NG) - 234
    - Oman (OM) - 968
    - Pakistan (PK) - 92
    - Peru (PE) - 51
    - Poland (PL) - 48
    - Qatar (QA) - 974
    - Romania (RO) - 40
    - Russia (RU) - 7
    - Saudi Arabia (SA) - 966
    - Singapore (SG) - 65
    - Sri Lanka (LK) - 94
    - South Africa (ZA) - 27
    - Spain (ES) - 34
    - Turkey (TR) - 90
    - Ukraine (UA) - 380
    - United Arab Emirates (AE) - 971
    - United Kingdom (GB) - 44
- **Charged based on regional rates** – 8 pricing regions
    - **North America – 2 markets**
        - Canada (CA) - 1
        - United States (US) - 1
    - **Rest of Africa – 40 markets**
        - Algeria (DZ) - 213
        - Angola (AO) - 244
        - Benin (BJ) - 229
        - Botswana (BW) - 267
        - Burkina Faso (BF) - 226
        - Burundi (BI) - 257
        - Cameroon (CM) - 237
        - Chad (TD) - 235
        - Republic of the Congo (CG) - 242
        - Eritrea (ER) - 291
        - Ethiopia (ET) - 251
        - Gabon (GA) - 241
        - Gambia (GM) - 220
        - Ghana (GH) - 233
        - Guinea-Bissau (GW) - 245
        - Ivory Coast (CI) - 225
        - Kenya (KE) - 254
        - Lesotho (LS) - 266
        - Liberia (LR) - 231
        - Libya (LY) - 218
        - Madagascar (MG) - 261
        - Malawi (MW) - 265
        - Mali (ML) - 223
        - Mauritania (MR) - 222
        - Mozambique (MZ) - 258
        - Namibia (NA) - 264
        - Niger (NE) - 227
        - Rwanda (RW) - 250
        - Senegal (SN) - 221
        - Sierra Leone (SL) - 232
        - Somalia (SO) - 252
        - South Sudan (SS) - 211
        - Sudan (SD) - 249
        - Eswatini (SZ) - 268
        - Tanzania (TZ) - 255
        - Togo (TG) - 228
        - Tunisia (TN) - 216
        - Uganda (UG) - 256
        - Zambia (ZM) - 260
        - Zimbabwe (ZW) - 263
    - **Rest of Asia Pacific – 16 markets**
        - Afghanistan (AF) - 93
        - Australia (AU) - 61
        - Cambodia (KH) - 855
        - China (CN) - 86
        - Japan (JP) - 81
        - Laos (LA) - 856
        - Mongolia (MN) - 976
        - New Zealand (NZ) - 64
        - Papua New Guinea (PG) - 675
        - Philippines (PH) - 63
        - Taiwan (TW) - 886
        - Tajikistan (TJ) - 992
        - Thailand (TH) - 66
        - Turkmenistan (TM) - 993
        - Uzbekistan (UZ) - 998
        - Vietnam (VN) - 84
    - **Rest of Central &amp; Eastern Europe – 16 markets**
        - Albania (AL) - 355
        - Armenia (AM) - 374
        - Azerbaijan (AZ) - 994
        - Belarus (BY) - 375
        - Bulgaria (BG) - 359
        - Croatia (HR) - 385
        - Czech Republic (CZ) - 420
        - Georgia (GE) - 995
        - Greece (GR) - 30
        - Latvia (LV) - 371
        - Lithuania (LT) - 370
        - Moldova (MD) - 373
        - North Macedonia (MK) - 389
        - Serbia (RS) - 381
        - Slovakia (SK) - 421
        - Slovenia (SI) - 386
    - **Rest of Western Europe – 9 markets**
        - Austria (AT) - 43
        - Belgium (BE) - 32
        - Denmark (DK) - 45
        - Finland (FI) - 358
        - Ireland (IE) - 353
        - Norway (NO) - 47
        - Portugal (PT) - 351
        - Sweden (SE) - 46
        - Switzerland (CH) - 41
    - **Rest of Latin America – 15 markets**
        - Bolivia (BO) - 591
        - Costa Rica (CR) - 506
        - Dominican Republic (DO) - 1 (809, 829, 849)
        - Ecuador (EC) - 593
        - El Salvador (SV) - 503
        - Guatemala (GT) - 502
        - Haiti (HT) - 509
        - Honduras (HN) - 504
        - Jamaica (JM) - 1 (658, 876)
        - Nicaragua (NI) - 505
        - Panama (PA) - 507
        - Paraguay (PY) - 595
        - Puerto Rico (PR) - 1 (787, 939)
        - Uruguay (UY) - 598
        - Venezuela (VE) - 58
    - **Rest of Middle East – 4 markets**
        - Bahrain (BH) - 973
        - Jordan (JO) - 962
        - Lebanon (LB) - 961
        - Yemen (YE) - 967
    - **Other – All other markets**

## Prior updates to pricing and rates &#123;#prior-updates-to-pricing-and-rates&#125;

### Ongoing &#123;#ongoing&#125;

This section outlines ongoing pricing or billing updates for the WhatsApp Business Platform.

#### Billing localization for Brazil &#123;#billing-localization-for-brazil&#125;

**Warning:** For Brazil, gradual roll-out began as planned on July 1, 2026. As of July 16, 2026, all eligible Solution Providers and directly-integrated businesses can create new Messaging accounts in BRL.

- Effective July 1, 2026, as of 9am PT – Only Solution Providers and directly-integrated businesses whose Sold-To country is Brazil in [Billing Hub](https://business.facebook.com/billing_hub/legal_entities) (eligible customers) can create new Messaging accounts in BRL (Brazilian Reals). Learn more about [billing localization for Brazil](https://www.facebook.com/business/help/4344414845795884).
- Per-message rates in BRL are published in our [rate cards and volume tiers](#rate-cards-and-volume-tiers). Charges from any BRL Messaging account will be invoiced in BRL by Meta&#039;s local entity in Brazil, Facebook Brasil.
- As a reminder, eligible customers must ensure all Messaging accounts in their business portfolio are migrated to BRL **by June 30, 2027** to avoid disruptions, since as of July 1, 2027 Meta will no longer deliver the messages of non-BRL Messaging accounts of eligible customers. To make this migration process easier and faster, use the [Currency Migration API](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/change-billing-currency), which is available as of June 1, 2026.

#### Billing localization for India &#123;#billing-localization-for-india&#125;

- Billing localization launched on January 1, 2026 for Solution Providers and directly-integrated businesses whose Sold-To country is India in [Billing Hub](https://business.facebook.com/billing_hub/legal_entities) (eligible customers). Learn more about [billing localization for India](https://www.facebook.com/business/help/2301408543603167).
- Eligible customers must ensure all Messaging accounts in their business portfolio are migrated to INR **by December 31, 2026** to avoid disruptions, since as of January 1, 2027 Meta will no longer deliver the messages of non-INR Messaging accounts of eligible customers. To make this migration process easier and faster, use the [Currency Migration API](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/change-billing-currency), which is available as of June 1, 2026.

### Prior updates &#123;#prior-updates&#125;

This section outlines prior pricing or billing updates for the WhatsApp Business Platform over the last 12 months.

#### Effective October 1, 2026 &#123;#effective-october-1-2026&#125;

##### 1. Charging for messages that were previously free &#123;#charging-for-previously-free-messages&#125;

**Warning:** For any Solution Provider or directly-integrated businesses that do not have a payment method on file by September 30, 2026, Meta will stop delivering service messages as of when they become charged on October 1, 2026. To avoid disruptions to your service messages, please [add a payment method](https://business.facebook.com/latest/billing_hub/payment_methods/) for your Messaging account(s) by September 30, 2026.

Meta resumed charging, on a per-message basis, for messages that were previously free: 

- Service messages, which became free as of Nov. 1, 2024. How Meta charges for these messages is outlined [above](#charges-by-message-category). Additionally, Meta introduced a [free monthly tier](#free-tier-of-monthly-service-messages) of service messages per business phone number.
- Utility messages sent in response to users (thus in an open [customer service window](#customer-service-window-csw)), which became free as of July 1, 2025. How Meta charges for these messages is outlined [above](#charges-by-message-category). For messages with a pricing category (`&lt;PRICING_CATEGORY&gt;`) of utility that are sent in an open [customer service window](#customer-service-window-csw), the pricing type (`&lt;PRICING_TYPE&gt;`) in the pricing object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks changed from `free_customer_service` to `regular` as of October 1, 2026.

##### 2. Oct. ‘26 rate card updates &#123;#oct-2026-rate-card-updates&#125;

Meta updated 40 rates, as summarized and in the table below:

- _Moved markets out of their respective “Rest Of” region to be named on the rate card_ – 9 markets.
    - Across message categories – Until September 30, 2026, messages to users in these markets were charged the respective regional rates (for example, Rest of Middle East for Kuwait). These markets have been moved out of regional rate pricing to be named on rate cards, with market-specific rates.
    - For utility and authentication messages – Volume tiers for these markets became market-specific. For example, messages businesses send to users in Kuwait a/ no longer count toward the volume tiers of Rest of Middle East and instead b/ count toward the volume tiers of Kuwait.

| Pricing element | Until Sep. 30, 2026 | As of Oct. 1, 2026 |
| --- | --- | --- |
| Rate charged | Rate of respective &quot;Rest Of&quot; pricing region | Rate of newly-standalone market |
| Accrual for volume tiers | Toward volume tiers of respective &quot;Rest Of&quot; pricing region | Toward volume tiers specific of newly-standalone market |
| Example | Morocco was charged “Rest of Africa” rate&lt;br&gt;Messages to users in Morocco contributed to “Rest of Africa” volume tiers | Morocco is charged its rate&lt;br&gt;Messages to users in Morocco count toward Morocco’s volume tiers |

- _Marketing_: 7 markets, with 7 increases and 0 decreases.
- _Utility, authentication_: 12 markets, with 8 increases and 4 decreases.
- _Authentication-International_: 9 markets with new rates (see section 3 below).

| Effective date | Market | Category | Change in rate | Note |
| --- | --- | --- | --- | --- |
| October 1, 2026 | Bangladesh | Utility&lt;br&gt;Authentication | Decrease | Moved out of “Rest of Asia Pacific” region |
| October 1, 2026 | Bangladesh | Auth-int’l | New | Moved out of “Rest of Asia Pacific” region |
| October 1, 2026 | Iraq | Utility&lt;br&gt;Authentication | Decrease | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Iraq | Auth-int’l | New | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Kazakhstan | Utility&lt;br&gt;Authentication | Increase | Moved out of “Other” region |
| October 1, 2026 | Kazakhstan | Auth-int’l | New | Moved out of “Other” region |
| October 1, 2026 | Kuwait | Marketing | Increase | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Kuwait | Utility&lt;br&gt;Authentication | Increase | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Kuwait | Auth-int’l | New | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Mexico | Marketing | Increase | – |
| October 1, 2026 | Morocco | Marketing&lt;br&gt;Utility&lt;br&gt;Authentication | Increase | Moved out of “Rest of Africa” region |
| October 1, 2026 | Morocco | Auth-int’l | New | Moved out of “Rest of Africa” region |
| October 1, 2026 | Nepal | Utility&lt;br&gt;Authentication | Decrease | Moved out of “Rest of Asia Pacific” region |
| October 1, 2026 | Nepal | Auth-int’l | New | Moved out of “Rest of Asia Pacific” region |
| October 1, 2026 | Oman | Utility&lt;br&gt;Authentication | Increase | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Oman | Auth-int’l | New | Moved out of “Rest of Middle East” region |
| October 1, 2026 | Pakistan | Utility&lt;br&gt;Authentication | Increase | – |
| October 1, 2026 | Peru | Utility&lt;br&gt;Authentication | Increase | – |
| October 1, 2026 | Rest of Asia Pacific | Marketing | Increase | – |
| October 1, 2026 | Rest of Middle East | Marketing | Increase | – |
| October 1, 2026 | Saudi Arabia | Marketing | Increase | – |
| October 1, 2026 | South Africa | Utility&lt;br&gt;Authentication | Increase | – |
| October 1, 2026 | Sri Lanka | Utility&lt;br&gt;Authentication | Decrease | Moved out of “Rest of Asia Pacific” region |
| October 1, 2026 | Sri Lanka | Auth-int’l | New | Moved out of “Rest of Asia Pacific” region |
| October 1, 2026 | Ukraine | Utility&lt;br&gt;Authentication | Increase | Moved out of “Rest of Central &amp; Eastern Europe” region |
| October 1, 2026 | Ukraine | Auth-int’l | New | Moved out of “Rest of Central &amp; Eastern Europe” region |
| October 1, 2026 | United Arab Emirates | Marketing | Increase | – |

##### 3. New authentication-international rates in 9 markets &#123;#new-authentication-international-rates&#125;

These are higher than the utility and authentication rates in these markets, aligned to industry standards. This means:

- There is no change to how Meta determines eligibility for authentication-international rates. Learn more about [authentication-international eligibility](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates#eligibility).
    - _Effective September 1, 2026_ – Meta determines eligibility based on authentication messages delivered across not 9 but 18 markets with authentication-international rates, including the additional 9 markets with a new authentication-international rate as of Oct. 1, 2026.
    - _Effective October 1, 2026_ – Business may be charged authentication-international rates in up to +9 markets or begin to be charged authentication-international rates, per the table below.

| As of Aug. 30, 2026 | As of Sep. 1, 2026 | As of Oct. 1, 2026 |
| --- | --- | --- |
| **Eligible for auth-int’l rates.**&lt;br&gt;Thus, charged auth-int’l rates in up to 9 markets1 | No change; existing eligibility applies to new markets with auth-int’l rates | Charged auth-int’l rates in up to 9 additional markets, thus up to 18 markets |
| **Not yet eligible for auth-int’l rates.**&lt;br&gt;Thus, not charged auth-int’l rates in any markets | May become eligible for auth-int’l rates, per messages across not 9 but 18 markets2 | Charged auth-int’l rates in up to 18 markets |

1 Per their [Primary Business Location](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates#primary-business-location), businesses may continue to be charged the authentication rate in one of these 18 markets

2 Meta continues to provide a 30-day [eligibility notice](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates#eligibility-email) to all admins of newly-eligible Messaging account(s) before authentication-international charges begin. This provides time for businesses to set their Primary Business Location.

#### Effective July 1, 2026 &#123;#effective-july-1-2026&#125;

Meta updated the 16 rates, as summarized and in the table below:

- _Moved markets out of their respective “Rest Of” region to be named on the rate card_ – 6 markets.
    - Across message categories – Until June 30, 2026, messages to users in these markets were charged the respective regional rates (for example, Rest of Central and Eastern Europe for Poland). These markets have been moved out of regional rate pricing to be named on rate cards, with market-specific rates.
    - For utility and authentication messages – Volume tiers for these markets became market-specific. For example, messages businesses send to users in Poland a/ no longer count toward the volume tiers of Rest of Central and Eastern Europe and instead b/ count toward the volume tiers of Poland.

| Pricing element | Until Jun. 30, 2026 | As of Jul. 1, 2026 |
| --- | --- | --- |
| Rate charged | Rate of respective &quot;Rest Of&quot; pricing region | Rate of newly-standalone market |
| Accrual for volume tiers | Toward volume tiers of respective &quot;Rest Of&quot; pricing region | Toward volume tiers specific of newly-standalone market |
| Example | Singapore was charged “Rest of Asia Pacific” rate&lt;br&gt;Messages to users in Singapore contributed to “Rest of Asia Pacific” volume tiers | Singapore is charged its rate&lt;br&gt;Messages to users in Singapore count toward Singapore’s volume tiers |

- _Marketing_: 4 markets, with 3 increases and 1 decrease.
- _Utility, authentication_: 6 markets, with 5 increases and 1 decrease.
- _Authentication-International_: No changes.

| Effective date | Market | Category | Change in rate | Note |
| --- | --- | --- | --- | --- |
| July 1, 2026 | Hong Kong | Utility&lt;br&gt;Authentication | Higher | Moved out of “Rest of Asia Pacific” region |
| July 1, 2026 | Hungary | Utility&lt;br&gt;Authentication | Higher | Moved out of “Rest of Central &amp; Eastern Europe” region |
| July 1, 2026 | Italy | Marketing | Higher | – |
| July 1, 2026 | Poland | Marketing&lt;br&gt;Utility&lt;br&gt;Authentication | Lower | Moved out of “Rest of Central &amp; Eastern Europe” region |
| July 1, 2026 | Qatar | Utility&lt;br&gt;Authentication | Higher | Moved out of “Rest of Middle East” region |
| July 1, 2026 | Romania | Utility&lt;br&gt;Authentication | Higher | Moved out of “Rest of Central &amp; Eastern Europe” region |
| July 1, 2026 | Singapore | Utility&lt;br&gt;Authentication | Higher | Moved out of “Rest of Asia Pacific” region |
| July 1, 2026 | Spain | Marketing | Higher | – |
| July 1, 2026 | United Kingdom | Marketing | Higher | – |

#### Effective April 1, 2026 &#123;#effective-april-1-2026&#125;

Meta updated the 6 rates, as summarized and in the table below:

- _Marketing_: 1 market, with 1 increase.
- _Utility, authentication_: 2 markets, with 1 increase and 1 decrease.
- _Authentication-International_: 1 market, with 1 increase.

| Effective date | Market | Category | Change in rate |
| --- | --- | --- | --- |
| April 1, 2026 | India | Auth-int’l | Higher |
| April 1, 2026 | Pakistan | Utility&lt;br&gt;Authentication | Higher |
| April 1, 2026 | Saudi Arabia | Marketing | Higher |
| April 1, 2026 | Turkey | Utility&lt;br&gt;Authentication | Lower |

#### Effective January 1, 2026 &#123;#effective-january-1-2026&#125;

Meta updated the 5 rates, as summarized and in the table below:

- _Marketing_: 3 markets, with 1 increase and 2 decreases.
- _Utility, authentication_: 1 market, with 0 increases and 1 decrease.
- _Authentication-International_: No changes.

| Effective date | Market | Category | Change in rate |
| --- | --- | --- | --- |
| January 1, 2026 | Egypt | Marketing | Lower |
| January 1, 2026 | France | Marketing | Lower |
| January 1, 2026 | India | Marketing | Higher |
| January 1, 2026 | North America | Utility&lt;br&gt;Authentication | Lower |

#### Effective October 1, 2025 &#123;#effective-october-1-2025&#125;

In September 2025, alongside announcing Oct.1 ‘25 rate card updates, Meta published its [pricing calendar](#pricing-calendar), which applies going forward.

Meta updated the 13 rates, as summarized and in the table below:

- _Marketing_: 2 markets, with 1 increase and 1 decrease.
- _Utility, authentication_: 4 markets, with 1 increase and 3 decreases.
- _Authentication-International_: No changes.
- _Moved markets to a different “Rest Of”_: 1 market

| Effective date | Market | Category | Change in rate | Note |
| --- | --- | --- | --- | --- |
| October 1, 2025 | Argentina | Utility&lt;br&gt;Authentication | Lower | – |
| October 1, 2025 | Colombia | Utility&lt;br&gt;Authentication | Higher | – |
| October 1, 2025 | Egypt | Utility&lt;br&gt;Authentication | Lower | – |
| October 1, 2025 | Mexico | Marketing | Lower | – |
| October 1, 2025 | Saudi Arabia | Utility&lt;br&gt;Authentication | Lower | – |
| October 1, 2025 | United Arab Emirates | Marketing | Higher | – |
| October 1, 2025 | Zimbabwe | All | – | Moved from “Other” to “Rest of Africa” region1 |

1 Thus, messages delivered to WhatsApp users with a +263 country calling code (Zimbabwe) will be charged “Rest of Africa” rates.

#### Effective July 1, 2025 or prior &#123;#effective-july-1-2025-or-prior&#125;

- Effective July 1, 2025 – Lower utility and authentication message rates across several markets, to ensure pricing is on-par to alternate channels for these use cases. Marketing conversation rates became marketing message rates.
- Effective April 1, 2025 – Lowered [authentication-international conversation rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates) for Egypt, Nigeria, Pakistan, and South Africa.
- Effective February 1, 2025 – Lowered [authentication conversation rates](#what-meta-charges-for-messages) for Egypt, Malaysia, Nigeria, Pakistan, Saudi Arabia, South Africa, and the United Arab Emirates.
- Effective November 1, 2024 – [Service conversations](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/conversation-based-pricing#service-conversations) are now free for all businesses.
- Effective October 1, 2024 – Updated [marketing conversation rates](#what-meta-charges-for-messages) in India, Saudi Arabia, the United Arab Emirates, and the United Kingdom.
- Effective August 1, 2024 – Lowered [utility conversation rates](#what-meta-charges-for-messages).

## Other pricing topics &#123;#other-pricing-topics&#125;

### Marketing – Max-price feature for Marketing Messages API for WhatsApp &#123;#marketing-max-price-feature-for-marketing-messages-api-for-whatsapp&#125;

Starting in 2026, businesses integrated into Marketing Messages API for WhatsApp can choose to set a [max-price](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/pricing) per marketing message delivery; when a max-price is set, Meta will charge that max-price or lower for delivery.

### Service – Pricing policy for AI Providers leveraging WhatsApp Business Platform &#123;#service-pricing-policy-for-ai-providers-leveraging-whatsapp-business-platform&#125;

See the [AI Providers pricing policy](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers), effective February 16, 2026 and updated as of May 12, 2026. Pricing updates for service messages launching October 1, 2026 do not apply to AI Providers; see the [AI Providers pricing policy](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers) for how Meta charges them for service messages.

### Service - Pricing policy for eligible governments and non-profits using the WhatsApp Business Platform &#123;#service-pricing-policy-for-eligible-governments-and-non-profits&#125;

Starting October 1, 2026 - Service messages remain free beyond the monthly free tier only for eligible government and non-profit organizations using the WhatsApp Business Platform. This pricing policy will be in effect through December 31, 2027.

Meta continues to support governments and non-profit organizations, and this policy allows Meta to enable eligible governments and non-profits to maintain an always-on presence on WhatsApp, to respond to and engage with WhatsApp users.

Eligible organizations include:

- Government departments and agencies; inter-governmental organizations
- Community non-profit organizations, including those in public health, crisis response, disaster relief and non-partisan civic engagement

For organizations Meta has identified as eligible, this policy will apply as of 12am by Messaging account timezone on October 1, 2026.

#### Understand if you are eligible &#123;#understand-if-you-are-eligible&#125;

There are two ways for Solution Providers and businesses to understand eligibility for this policy:

- As of October 12, 2026, via webhooks. Ingest the new `subtype` field to build a view of which Messaging accounts are eligible.
- As of October 23, 2026, via the `service_pricing_policy` field. This scales better: you can query any or all of the Messaging accounts you manage, and Meta confirms which are eligible.

**New `subtype` field in webhooks**

Status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks include a new `subtype` field in the pricing object. Service messages that are free because the organization is eligible for this policy have `subtype` set to `paid_exempt`.

Example pricing object in a [status messages webhook](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status), for a service message from an eligible government or non-profit organization:

```json
&#123;
  &quot;pricing&quot;: &#123;
    &quot;billable&quot;: false,
    &quot;pricing_model&quot;: &quot;PMP&quot;,
    &quot;category&quot;: &quot;service&quot;,
    &quot;type&quot;: &quot;free_customer_service&quot;,
    &quot;subtype&quot;: &quot;paid_exempt&quot;
  &#125;
&#125;
```

- `type` is `free_customer_service`, or `free_group_customer_service` for group messages.
- `subtype` is `paid_exempt` when the service message is free because the organization is eligible for this policy.

**New `service_pricing_policy` field on accounts**

To check whether a Messaging account is eligible:

```html
GET /&lt;WHATSAPP_BUSINESS_ACCOUNT_ID&gt;?fields=id,name,service_pricing_policy
```

Get the value for Messaging accounts your business portfolio owns or manages on behalf of your clients:

```html
GET /&lt;BUSINESS_PORTFOLIO_ID&gt;/owned_whatsapp_business_accounts?fields=id,name,service_pricing_policy
GET /&lt;BUSINESS_PORTFOLIO_ID&gt;/client_whatsapp_business_accounts?fields=id,name,service_pricing_policy
```

Based on the results, you can understand which Messaging accounts are eligible:

- **Eligible** if `service_pricing_policy` is `PAID_EXEMPT`. Service messages from this Messaging account are free under this policy.
- **Not eligible** if `service_pricing_policy` is `REGULAR`. These Messaging accounts would be charged at [published rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#what-meta-charges-for-messages) for service messages as of October 1, 2026, and still benefit from the [free monthly tier of service messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#free-tier-of-monthly-service-messages).

#### Request a review of eligibility &#123;#request-a-review-of-eligibility&#125;

Meta is also building a way for Solution Providers and businesses to request a review of their eligibility for this policy, and will provide an update once it is available.

### Calling – WhatsApp Business Calling API pricing &#123;#calling-whatsapp-business-calling-api-pricing&#125;

The WhatsApp Business Calling API has different pricing. See our [Calling API pricing document](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/pricing) to learn more.

### Conversation-based pricing &#123;#conversation-based-pricing&#125;

[Conversation-based pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/conversation-based-pricing) is deprecated. It was replaced with per-message pricing on July 1, 2025.

## Analytics &#123;#analytics&#125;

Use the [`pricing_analytics` field](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics) to get per-message pricing breakdowns and tiering information for delivered messages.

## Pricing webhooks &#123;#pricing-webhooks&#125;

Billable messages have `type` set to `regular` in the pricing object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;&lt;PRICING_CATEGORY&gt;&quot;
&#125;
```

The `&lt;PRICING_CATEGORY&gt;` tells you what rate was applied (for example, marketing). See the status messages webhook reference for a list of possible values.

Note that currently, tiering information is not included in any webhooks. Use the [`pricing_analytics` field](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics) to get tiering information for delivered messages.

## Billing &#123;#billing&#125;

Billing and billing-related actions are handled through the Meta Business Suite. See [About Billing For Your WhatsApp Business Account](https://www.facebook.com/business/help/2225184664363779) for more information.

### Billing attribution with multiple Messaging accounts &#123;#billing-attribution-with-multiple-messaging-accounts&#125;

When several Messaging accounts send on the same business phone number, charges are attributed to the specific Messaging account that sent each message. The `messaging_account_id` — passed on the send message API call, or resolved from your app token — determines which Messaging account is billed for a given template message delivery.

- Each Messaging account maintains its own billing relationship, payment method, and spend limits, regardless of how many other Messaging accounts send on the same phone number.
- Volume tiers are calculated at the business portfolio level across all Messaging accounts the portfolio owns, not per phone number.
- Solution Providers are charged only for messages sent through their own Messaging account. Messages sent by other partners on the same phone number do not appear on their invoice.



---

Full documentation index for this product: https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt
