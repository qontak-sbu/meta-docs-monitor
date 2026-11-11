# Upcoming pricing updates for Meta Business Agent, service and utility messages


**Warning:** This page explains upcoming pricing updates for the Meta Business Platform. To understand how we currently charge, please see [Pricing on the WhatsApp Business Platform](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing).

**Warning:** For any Solution Provider or directly-integrated businesses that does _not_ have a payment method on file by September 30, 2026, Meta will *stop delivering service messages* as of when they become charged on October 1, 2026. To avoid disruptions to your service messages, please [add a payment method](https://business.facebook.com/latest/billing_hub/payment_methods/) for your Messaging account(s) by September 30, 2026.

Non-template messages (service message or Meta Business Agent message) can only be sent in an open 24-hour [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows), which opens and resets with each user message. Thus non-template messages can only be used to respond - not reach out - to users

## Message categories for non-template messages

Until July 1, 2026: All non-template message responses to users were service messages (`category: service`). 

With the launch of Meta Business Agent on July 1, 2026: Non-template messages can be one of two categories -- Service (existing category) or Meta Business Agent (new category).

- **Meta Business Agent messages** – Powered by the Meta Business Agent Platform. This is a new message category on our platform.
- **Service messages** – Can be powered by a person, like a customer service representative, or by a 3rd-party AI solution. This is an existing message category on our platform. Any non-template message that is _not_ powered by Meta Business Agent is a service message.

### How Meta charges across message types

**Warning:** This pricing explainer encompasses the pricing updates highlighted on this page: Meta Business Agent pricing guide (PDF)

Meta charges for messages from businesses to WhatsApp users only, and only when the message is delivered (vs. sent). Meta charges based on the category of the message, per below: 

_Template messages_
- **Marketing, utility, authentication** - Meta charges on a per-message basis, aligned to industry standards. Rates by market and message category vary.

_Non-template messages_
- **Service** - Meta charges on a per-message basis, aligned to industry standards. Rates by market and message category vary.
- **Meta Business Agent** - Meta charges on a per-message basis, with one token-based charge that encompasses both AI agent processing (token consumption) and message delivery. Charging for token consumption aligns to industry standards. However, Meta only charges for input and output tokens, and does not charge for cache tokens. 

Note: Businesses that use a third-party AI solution typically incur separate charges for AI usage from the AI provider and message delivery from the messaging solution provider.


## Upcoming pricing updates

In H2&#039;2026, Meta will introduce these pricing updates as part of continued efforts to ensure pricing reflects the value these messages deliver to businesses:

- **Effective August 1, 2026** - Meta will charge on a per-token basis for **Meta Business Agent messages**. Meta will apply one charge that encompasses both token consumption (input and output tokens only) and message delivery.
- **Effective October 1, 2026** - Meta will charge on a per-message basis for all **service messages**, consistent with how Meta charges for template messages. These messages have not been charged since November 1, 2024.
- **Effective October 1, 2026** - Meta will charge on a per-message basis for **utility messages sent in response to users** (within an open 24-hour customer service window). These messages have not been charged since July 1, 2025.

The following table summarizes how Meta charges (or will charge) by message category.

| Message category | Marketing | Utility | Authentication | Service | Meta Business Agent |
| --- | --- | --- | --- | --- | --- |
| Business objective | Reach out to a user | Reach out to a user | Reach out to a user | Respond to a user | Respond to a user |
| Message type | Template1 | Template1 | Template1 | Non-template | Non-template |
| When it can be sent | At any time | At any time | At any time | In an open CSW2 | In an open CSW2 |
| Who powers the message | Business triggers delivery | Business triggers delivery | Business triggers delivery | Person or 3rd-party AI | Meta Business Agent Platform |
| Does Meta charge? | Yes | Yes | Yes | As of Oct. 1, 2026 | As of Aug. 1, 2026 |
| How does Meta charge? | Per message | Per message | Per message | Per message | Per token |
| Does Meta charge for AI usage? | n/a | n/a | n/a | n/a - 3rd-party AI charges the business | Yes - one token-based charge |
| Does Meta charge for message delivery? | Yes | Yes | Yes | Yes | Yes - one token-based charge |
| Is this message free in the FEP3? | Yes | Yes | Yes | Yes | No |

1. Template messages are categorized per our [template category guidelines](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization)
2. Within the 24-hour [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows), which opens and resets with each user message
3. Within the [free entry point window](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#free-entry-point-windows-fep), during which any marketing, utility, authentication or service message is not charged

### Rates

#### Meta Business Agent messages

- **Charge for**: Delivered message.
- **Meter**: Per message, based on *one per-token charge* that encompasses AI agent processing (token consumption, for input and output tokens only) and message delivery.
- **Rate**: One global rate of $2.00 USD per 1 million (M) tokens. One message typically consumes 20,000–25,000 tokens, which translates to approximately 4–5 cents (USD) per message.
- **Cost per message**: Varies with complexity. Simple responses consume fewer tokens and cost less; complex responses consume more tokens and cost more.

The following table shows example interactions and their estimated cost.

| Type of interaction | Example user message | Messages to the user | Tokens consumed | Estimated cost |
| --- | --- | --- | --- | --- |
| Simple inquiry | &quot;At what time do you open?&quot; | 4 | ~80,000 (~20,000/message) | ~16–20 cents |
| Complex interaction | &quot;I&#039;m stuck on step 3 of this assembly—can you walk me through it?&quot; | 10 | ~250,000 (~25,000/message) | ~40–50 cents |

#### Service messages
**Warning:** For any Solution Provider or directly-integrated businesses that does _not_ have a payment method on file by September 30, 2026, Meta will stop delivering service messages as of when they become charged on October 1, 2026. To avoid disruptions to your service messages, please [add a payment method](https://business.facebook.com/latest/billing_hub/payment_methods/) for your Messaging account(s) by September 30, 2026.

**Warning:** To-be rates for service messages becoming effective October 1, 2026 are [now published](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#updates-to-rate-cards), as of September 1, 2026, per our published pricing calendar and the guidance we provided as of our July 1, 2026 announcement.

- **Charge for**: Delivered message.
- **Meter**: Per message.
- **Rate**: By market, rates for service messages will be the same as the rates for utility and authentication messages. To-be rates for service messages are [now published](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#updates-to-rate-cards).
- **Cost per message**: Fixed, per published rates. 
- **Volume tiers**: None. Meta will not offer volume tiers for service messages. Meta continues to offer [volume tiers for utility and authentication messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#rate-cards-and-volume-tiers).
- **Frequency of updates**: Consistent with the [pricing calendar](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#pricing-calendar), Meta may update rates up to quarterly. Meta will announce and publish the rates that take effect October 1, 2026, including rates for service messages, by September 1, 2026.

### Pricing example

Below is an example of an interaction between a business and a user. It starts with the business reaching out with a marketing template, using Meta Business Agent to respond to user questions, escalating to a customer service rep, and ultimately sending an order confirmation, all within one hour.

- *As of July 1, 2026:* Meta charges only for 1 marketing template message.
- *As of August 1, 2026:* Meta charges for 3 messages (1 marketing, 2 Meta Business Agent).
- *As of October 1, 2026:* Meta will charge for each message the business sends – 5 messages thus 5 charges (1 marketing, 2 Meta Business Agent, 1 service, 1 utility).

| Sender | Message content | Message type | Message category | Charge as of August 1, 2026 | Charge as of October 1, 2026 |
| --- | --- | --- | --- | --- | --- |
| Business | Cart abandonment reminder | Template | Marketing | 1 marketing charge | 1 **marketing** charge |
| User | &quot;Do you have this in a Small?&quot; | — | — | Opens 24-hour CSW¹ | — |
| Business | Meta agentic response to user&#039;s question | Non-template | Meta Business Agent | 1 Meta Business Agent charge | 1 **Meta Business Agent** charge |
| User | &quot;Do you have this in white?&quot; | — | — | — | — |
| Business | Meta agentic response to user&#039;s question | Non-template | Meta Business Agent | 1 Meta Business Agent charge | 1 **Meta Business Agent** charge |
| User | &quot;I&#039;m ready to check-out, but my card is expired&quot; | — | — | — | — |
| *Meta Business Agent hands off to customer service rep* | | | | — | — |
| Business | Customer service rep responds to user&#039;s question | Non-template | Service | No charge | 1 **service** charge |
| Business | Order confirmation | Template | Utility | No charge | 1 **utility** charge |
| | | | **Total charges** | **3 charges** | **5 charges** |

### Cost comparison: Service vs. Meta Business Agent messages

**Warning:** Comparing the prices of service vs. Meta Business Agent messages is not an apples-to-apples comparison because businesses likely incur other costs to power service messages (whether they are powered by people or a 3rd-party AI solution). An accurate comparison should incorporate these non-Meta costs.

The following table compares the expected cost to send 1,000 AI-powered messages in response to users in Brazil. Estimates for third-party AI solutions are based on publicly available information and benchmarks. Message delivery costs are based on the current rate for utility and authentication messages to users in Brazil.

| Message category | Service | Service | Meta Business Agent |
| --- | --- | --- | --- |
| Model complexity | Lower complexity | Higher complexity | Higher complexity |
| AI agent cost | ~2 cents / mssg | ~9 cents / mssg | ~4–5 cents / mssg |
| Message delivery1 | 0.68 cents / mssg | 0.68 cents / mssg | ~4–5 cents / mssg |
| Total per message | ~2 – 3 cents | ~9 – 10 cents | ~4 – 5 cents |
| Total for 1,000 messages | ~$27 | ~$97 | ~$40 – $50 |

1. The 0.68 USD cent message delivery rate is based on the [current rate](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#rate-cards-and-volume-tiers) (as of July 1, 2026) for utility and authentication messages to users in Brazil. 

## Key things to remember

- **Any non-template message is charged as of October 1, 2026.** If the message is powered by Meta Business Agent, it incurs the charge of a Meta Business Agent message. If it is not powered by Meta Business Agent, it incurs the charge of a service message.
- **Only one charge applies per message.** A message to a user — template or non-template — has only one category and is charged only per that category. A non-template message is charged _either_ as a Meta Business Agent message _or_ as a service message, never both. This also applies to non-template messages with promotional content: Meta does not additionally apply a marketing template charge.
- **Not every Meta Business Agent message costs the same.** You pay proportionally to the value delivered: quick answers cost less (closer to ~4 cents per message), and rich, multi-turn problem-solving costs more (closer to ~5 cents per message).
- **The free entry point window is unchanged for message delivery.** Messages sent within the free entry point window, from ads that click to WhatsApp, remain free for message delivery. Meta Business Agent messages are still charged for token usage as of August 1, 2026.

## Billing for Meta Business Agent messages

**Warning:** As of August 1, 2026 at 12pm PT – Meta charges for Meta Business Agent messages, and a payment method is required in [Billing Hub](https://business.facebook.com/latest/billing_hub/) to use Meta Business Agent. For any business that does not have a payment method for their Meta Business Agent account, Meta will not deliver Meta Business Agent messages. The one exception is allowlisted testing: an agent whose `ai_audience` is set to `ALLOWLISTED_ONLY` can be turned on and will respond to consumers on its allowlist without a payment method attached, so a business can test before it sets up billing. Widening `ai_audience` to `EVERYONE` requires a payment method. See [Test your agent](https://developers.facebook.com/documentation/meta-business-agent/test-your-agent).

### Available payment methods

Consistent with industry norms, Meta charges businesses for Meta Business Agent, including those that access the WhatsApp Business Platform today via a Solution Provider(s). 

Businesses can pay for Meta Business Agent via:
- As of August 1, 2026 – Credit line with Meta, to be invoiced monthly. Available to eligible businesses only. 
- Starting September 8, 2026 – Credit/debit cards (Visa and Mastercard only). Available to all businesses. 

#### Credit line with Meta as a payment method
_For businesses that already have a credit line with Meta_, you can [add your Meta Business Agent account to this credit line](https://business.facebook.com/latest/billing_hub/credit_lines/) via Billing Hub. Once attached, your credit line will be reflected as a payment method for your Meta Business Agent account in the Accounts tab. 
- First, navigate to &#039;Credit lines&#039; in the side panel.
- Click the &#039;Set up now&#039; button in the modal for &#039;Use monthly invoicing for Business Agent.&#039;
- Accept payment and invoicing terms to add your Business Agent account to your existing credit line. 

_For businesses that do *not* have a credit line with Meta_, you may be eligible to [apply for a credit line](https://business.facebook.com/latest/billing_hub/credit_lines/) via Billing Hub. This is subject to review and approval by Meta. If you are not eligible and do not see the option to apply, credit/debit cards (available starting September 8, 2026) are your available payment method.
- First, click the &#039;Get started&#039; button in the &#039;Switch to monthly invoicing&#039; banner. 
- Follow the prompts on upcoming screens. On the &#039;Select accounts&#039; screen, ensure your Business Agent account remains selected. 
- Once approved, your credit line will appear in Billing Hub.  

#### Credit/debit card as a payment method
**Warning:** _Effective September 8, 2026_ – Credit and debit cards will become available as a payment method for Meta Business Agent. We previously shared this would launch on Sep. 15 for businesses in Brazil; that has been pulled forward to Sep. 8, 2026.

Credit or debit card as a payment method will be: 
- *Available* for businesses that do not yet have a payment method for Meta Business Agent. Once you [add a credit or debit card in Billing Hub](https://business.facebook.com/latest/billing_hub/payment_method/), this becomes how Meta will charge you for Meta Business Agent and you can [continue with Meta Business Agent set-up](https://developers.facebook.com/documentation/meta-business-agent/get-started#set-up-billing). 
- *Not available* for businesses that have already added their Meta Business Agent account to their credit line with Meta. These businesses will continue to be invoiced monthly for Meta Business Agent.


### Selecting a currency for your Business Agent account
As of July 1, 2026 - Meta has 16 currencies enabled on the WhatsApp Business Platform. You can create your Meta Business Agent account in one of these currencies, as outlined below. If you choose a non-USD Business Agent account, Meta will charge you in that currency. To determine charges in that currency, Meta will apply a daily exchange rate (FX) per the date each message was delivered to our [global USD rate](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages#meta-business-agent-messages). 

This is outlined in the table below:

| Your business&#039; Sold-To country in Billing Hub | Currency of your Business Agent account | Currency in which Meta invoices you | Rate Meta charges | Meta entity charging |
| --- | --- | --- | --- | --- |
| Any, except India or Brazil1 | USD | USD | Global USD rate | Meta Inc. (US-based) |
| Any, except India or Brazil1 | Other 13 currencies2 | Per MBA account&#039;s currency | Global USD rate × daily FX3 | Meta Ireland |
| India only | INR | INR | Global USD rate × daily FX3 | Facebook India |
| Brazil only | BRL | BRL if paying via card; USD if invoiced | Global USD rate × daily FX3 | Facebook Brazil if paying via card; Meta Inc. if invoiced |

1. Businesses whose Sold-To country in [Billing Hub](https://business.facebook.com/latest/billing_hub/credit_lines/) is India and Brazil can only choose respective local currencies of those markets
2. AED, ARS, AUD, CLP, COP, EUR, GBP, IDR, MXN, MYR, PEN, SAR, SGD
3. Exchange rate (FX) on the day each message was delivered



## Technical implementation

Service messages and Meta Business Agent messages use different analytics and webhook category values.

### Service messages

Service messages are an existing message category on the platform (`category: service`). You can use the [Pricing Analytics API](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics/#pricing-analytics) to understand how many service messages you have delivered. The category and charge for service messages are also included in message delivery webhooks.

**Analytics**

Query the `&lt;PRICING_CATEGORY&gt;` value of `SERVICE` to understand the count of service messages for a given timeframe.

```
&#123;
  &quot;start&quot;: &lt;START_TIMESTAMP&gt;,
  &quot;end&quot;: &lt;END_TIMESTAMP&gt;,
  &quot;phone_number&quot;: &quot;&lt;BUSINESS_PHONE_NUMBER&gt;&quot;,
  &quot;country&quot;: &quot;&lt;COUNTRY_CODE&gt;&quot;,
  &quot;pricing_type&quot;: &quot;REGULAR&quot;,
  &quot;pricing_category&quot;: &quot;SERVICE&quot;,
  &quot;volume&quot;: &lt;VOLUME&gt;,
  &quot;cost&quot;: &lt;COST&gt;
&#125;
```

**Webhooks**

The [webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#webhooks) reflect the `&lt;PRICING_CATEGORY&gt;` as `service`. Billable messages have `type` set to `regular` in the pricing object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks.

```
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;service&quot;
&#125;
```

### Meta Business Agent messages &#123;#meta-business-agent-messages-technical-implementation&#125;

**Analytics**

Use the [Business Agent Usage Insights API](https://developers.facebook.com/documentation/meta-business-agent/reference/insights/business-agent-usage-insights) to see the billable messages, billed tokens, and charges for your Meta Business Agent account over a date range, by hour, day, or month. Charges are calculated at the [Meta Business Agent rate](#meta-business-agent-messages).


---

Full documentation index for this product: https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt
