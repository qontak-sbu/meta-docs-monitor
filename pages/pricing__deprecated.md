# Pricing (deprecated)


**Warning:** Please refer to our [main pricing page](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing), which reflects updates effective as of October 1, 2026.

This document explains how pricing works on the WhatsApp Business Platform.

**Warning:** Pricing updates for Meta Business Agent, service, and utility messages will launch on August 1, 2026 and October 1, 2026. [Learn more](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages).

## Cloud API and Marketing Messages API for WhatsApp

Effective July 1, 2025, Meta charges on a **per-message basis** for messages businesses deliver to WhatsApp users:

- You are only charged when a [template message](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/overview) is *delivered* (`&quot;type&quot;:&quot;template&quot;`).
- Rates vary based on the template&#039;s [category](#message-template-categories) and the recipient WhatsApp phone number&#039;s [country calling code](#country-calling-codes).

Meta offers value to businesses in the following ways:

- As of November 1, 2024 - Meta does not charge for [non-template messages](#non-template-messages) (`&quot;type&quot;:&quot;text&quot;`, `&quot;type&quot;:&quot;image&quot;`, and so on). Non-template messages can only be sent within an open [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows). See [Sending messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#sending-messages) for a list of message types.
- As of July 1, 2025 - Meta does not charge for [utility templates in response to users](#Utility-template-messages-in-response-to-users) (delivered within an open customer service window).
- As of July 1, 2025 - You can unlock [lower rates](#volume-tiers) for utility and authentication template messages, based on messaging volume.
- Free entry point window - All messages are free within the [free entry point window](#free-entry-point-windows) that may extend up to 7 days.

## Pricing explainer
**Warning:** Pricing updates for Meta Business Agent, service, and utility messages will launch on August 1, 2026 and October 1, 2026. [Learn more](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages).

The pricing explainer PDF outlines how Meta charges businesses, in PDF form, and reflects updates launching October 1, 2026:
Pricing explainer (PDF)

## Message template categories

Template messages are the only message type that can be sent outside of a customer service window, to reach out to users. Templates can be categorized as:

- Marketing
- Utility
- Authentication

See [Template categorization](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization) to learn how template categorization works.

### Template messages vs. non-template messages

- CSW = [Customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows)
- FEP = [Free entry point window](#free-entry-point-windows)

**Warning:** Businesses are responsible for reviewing the category assigned to their approved templates. Whenever a template is used, a business accepts the charges associated with the category applied to the template at time of use.

## Charge example

In the example below, a business sends 4 messages to a WhatsApp user but is only charged for 2 (1 marketing charge, 1 utility charge).

| Hour | Action | Rate | Reason |
| --- | --- | --- | --- |
| 0 | You send a marketing template message to a WhatsApp user, promoting your new product. | Marketing | All marketing template messages are charged. |
| 2 | The user messages you about the product.&lt;br&gt;&lt;br&gt;This opens a 24 hour [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows) (&quot;CSW&quot;). | - | Messages sent from a WhatsApp user to a business are not charged. |
| 3 | You send a [text message](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/text-messages) to the user (`&quot;type&quot;:&quot;text&quot;`), describing the product in more detail. | None | All non-template messages are free within an open customer service window. |
| 4 | The user purchases the product and you send them a utility template confirming their order. | None | The CSW is still open, and utility templates sent within an open CSW are free. |
| 26 | The CSW closes, which means you can no longer send non-template messages. | - | 24 hours have passed since the user last messaged you. |
| 30 | You send a utility template message to the user, updating them on their order. | Utility | Utility template messages sent outside of a CSW are charged, and no open CSW exists between you and the user. |

## Billing attribution with multiple Messaging accounts

When several Messaging accounts send on the same business phone number, charges are attributed to the specific Messaging account that sent each message. The `messaging_account_id` — passed on the send message API call, or resolved from your app token — determines which Messaging account is billed for a given template message delivery.

- Each Messaging account maintains its own billing relationship, payment method, and spend limits, regardless of how many other Messaging accounts send on the same phone number.
- Volume tiers are calculated at the business portfolio level across all Messaging accounts the portfolio owns, not per phone number.
- Solution Partners are charged only for messages sent through their own Messaging account. Messages sent by other partners on the same phone number do not appear on their invoice.

## Pricing calendar

To better enable our customers to plan and prepare for pricing updates, the following pricing calendar applies for messaging and voice on the WhatsApp Business Platform:

- Meta may update pricing only _on the 1st day of each quarter_, thus up to 4 times per year: January 1, April 1, July 1, and/or October 1.
- Meta will provide advanced notice that is better aligned to the effort required to implement different types of pricing updates, per below:

| Type of pricing update | Examples | Minimum advance notice |
| --- | --- | --- |
| **Rate card update** | Updating the [rate](#rates) for a given market–product&lt;br&gt;&lt;br&gt;Updating the volume tiers for a given market–product (utility and authentication only)&lt;br&gt;&lt;br&gt;Moving a market from one [pricing region](#country-calling-codes) (for example, &quot;Other&quot;) to another or to be standalone on the rate card | 1 month |
| **Pricing model add-on** | Our July 1, 2025, introduction of new [volume tiers](#volume-tiers) for utility and authentication messages | 3 months |
| **Pricing model change** | Our July 1, 2025 update to our pricing model, from conversation-based pricing to per-message pricing | 6 months |

## Rates

Rates vary based on [template category](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization), [volume tier](#volume-tiers), and [country/region](#country-calling-codes) rate.

### Rate cards and volume tiers

These rate cards reflect our current rates and volume tiers, effective July 1, 2026, based on Messaging account timezone. This information is also available interactively on our [WhatsApp Business website](https://business.whatsapp.com/products/platform-pricing#rates).

| Currency | Rates(CSV) | Volume tiers(CSV) | Rates and Volume tiers(PDF) |
| --- | --- | --- | --- |
| USD | USD rates | USD volume tiers | USD rates and volume tiers |
| AED | AED rates | AED volume tiers | AED rates and volume tiers |
| ARS | ARS rates | ARS volume tiers | ARS rates and volume tiers |
| AUD | AUD rates | AUD volume tiers | AUD rates and volume tiers |
| BRL | BRL rates | BRL volume tiers | BRL rates and volume tiers |
| CLP | CLP rates | CLP volume tiers | CLP rates and volume tiers |
| COP | COP rates | COP volume tiers | COP rates and volume tiers |
| EUR | EUR rates | EUR volume tiers | EUR rates and volume tiers |
| GBP | GBP rates | GBP volume tiers | GBP rates and volume tiers |
| IDR | IDR rates | IDR volume tiers | IDR rates and volume tiers |
| INR | INR rates | INR volume tiers | INR rates and volume tiers |
| MXN | MXN rates | MXN volume tiers | MXN rates and volume tiers |
| MYR | MYR rates | MYR volume tiers | MYR rates and volume tiers |
| PEN | PEN rates | PEN volume tiers | PEN rates and volume tiers |
| SAR | SAR rates | SAR volume tiers | SAR rates and volume tiers |
| SGD | SGD rates | SGD volume tiers | SGD rates and volume tiers |

### Updates to rate cards

**Warning:** Below are future updates to our rates. See our [rate cards](#rate-cards-and-volume-tiers) above for current rates. 

Rate cards effective October 1, 2026 - including service rates - are [**now published below**](#rate-cards-effective-october-1-2026) and will be moved to our ‘Rate cards and volume tiers’ section as of October 1, 2026.

Rate updates below apply as of 12am by Messaging account timezone and encompass:

1. Quarterly [updates to rates](#updates-to-rates-effective-october-1-2026), for marketing, utility and authentication messages. 
    - Additionally, as [announced May 27, 2026](#as-announced-may-27-2026) to provide not 1-month notice but 4-month notice: Moving 9 markets out of respective “Rest Of” pricing region (marked with * below) with a new authentication-international rate in each of the 9 newly-standalone markets.
2. Charging for [service messages](#service-rates-effective-october-1-2026), with rates the same as those of utility and authentication, by market. 
    - [**New**] Additionally, Meta will introduce a free monthly tier of 1,000 service messages per business phone number. 
3. Charging for [utility messages in response to users](#utility-rates-effective-october-1-2026) (within the 24h customer service window), which have not been charged since July 1, 2025.

#### 1. Updates to rates, effective October 1, 2026 &#123;#updates-to-rates-effective-october-1-2026&#125;

**1a. Rate card updates, effective October 1, 2026**
- **Marketing** rates – Increases in Kuwait\*, Mexico, Morocco\*, Saudi Arabia, UAE, Rest of Middle East, Rest of Asia Pacific
- **Utility and authentication** rates – 
  - Increases in Kazakhstan\*, Kuwait\*, Morocco\*, Oman\*, Pakistan, Peru, South Africa, Ukraine\*. 
  - Decreases in Bangladesh\*, Iraq\*, Nepal\*, Sri Lanka\*.
- **Authentication-international** rates - New rates in Bangladesh\*, Iraq\*, Kazakhstan\*, Kuwait\*, Morocco\*, Nepal\*, Oman\*, Sri Lanka\*, Ukraine\*, as announced [on May 27, 2026](#as-announced-may-27-2026) to provide not 1-month but 4-month notice.

\* Market is being moved out of its respective &quot;Rest Of&quot; pricing region to be standalone on rate cards. The 9 with updates for utility, authentication and authentication-international rates were [announced May 27, 2026](#as-announced-may-27-2026).

**1b. Newly-standalone markets, effective October 1, 2026**

Meta [announced on May 27, 2026](#as-announced-may-27-2026) that 6 markets would be moved out of their respective &quot;Rest Of&quot; pricing region on July 1, 2026 and at least 9 other markets would be as of October 1, 2026. For those becoming standalone as of October 1, 2026, this means: 

| Charge | Until Sep. 30, 2026 | As of Oct. 1, 2026 |
| --- | --- | --- |
| Rate charged | Rate of respective &quot;Rest Of&quot; pricing region | Rate of newly-standalone market |
| Accrual for volume tiers | Volume tiers of respective &quot;Rest Of&quot; pricing region | Volume tiers specific of newly-standalone market |

**1c. Markets with a new [authentication-international rate](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates#countries-with-authentication-international-rates), effective October 1, 2026** 

- _Effective September 1, 2026_ – Per [below](#as-announced-may-27-2026), as announced on May 27, 2026, Meta will determine eligibility for authentication-international rates based on authentication messages across not 9 but 18 markets with authentication-international rates, including the additional 9 markets that will have an authentication-international rate as of Oct. 1, 2026.  
- _Effective October 1, 2026_ - Business may be charged authentication-international rates in up to +9 markets _or_ begin to be charged authentication-international rates, per the table below. 

| As of Aug. 30, 2026 | As of Sep. 1, 2026 | As of Oct. 1, 2026 |
| --- | --- | --- |
| Eligible for auth-int’l rates. Thus, charged auth-int’l rates in up to 9 markets1 | No change; existing eligibility applies to new markets with auth-int’l rates | Charged auth-int’l rates in up to 9 additional markets, thus up to 18 markets |
| Not yet eligible for auth-int’l rates. Thus, not charged auth-int’l rates in any markets | May become eligible for auth-int’l rates, per messages across not 9 but 18 markets2 | Charged auth-int’l rates in up to 18 markets |

1. Per their [Primary Business Location](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates#primary-business-location), businesses may continue to be charged the authentication rate in one of these 18 markets. 
2. Meta would continue to provide 30-day [eligibility notice](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates#eligibility-email) before authentication-international charges begin.


#### 2. Service rates, effective October 1, 2026 &#123;#service-rates-effective-october-1-2026&#125;

**Warning:** To-be service rates are [now published below](#rate-cards-effective-october-1-2026).

- _Effective October 1, 2026_ – Meta will charge on a per-message basis for service messages. As announced July 1, 2026, rates for service messages will be the same as those of utility and authentication, by market. Updates to utility and authentication rates (per above) are reflected in to-be service rates. 
- There is no change to when a service message can be sent - it still can only be sent in an open [24-hour customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows) which opens and resets with each user message.
- **(NEW)** _Effective October 1, 2026_ – Meta will introduce a monthly free tier for service messages. 
  1. Each business phone number has one shared free tier of 1,000 delivered service messages per month. Both 1:1 and group service deliveries draw from this same free tier. A 1:1 delivery consumes one unit; a group send consumes one unit per delivered recipient. Meta charges for service messages after the free tier has been used.  
  2. Unused service messages in the free tier do not roll over. The free tier resets monthly for each business phone number (for example, 1,000 for October with no roll-over; 1,000 for November with no roll-over).  
  3. If you do not have a payment method for your WhatsApp Business account, Meta _will_ deliver service messages within the shared free tier but _not_ deliver them after the free tier has been used. To ensure continuity of your service messages, please ensure you have a payment method in [Billing Hub](https://business.facebook.com/latest/billing_hub/).
- The only service message type that will continue to **not** be charged for all businesses as of October 1, 2026 is a [reaction message](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#message-types). These messages do not count toward the 1,000 free monthly service messages by business phone number. Separately, service messages remain free for [eligible governments and non-profits](#service-pricing-policy-for-eligible-governments-and-non-profits), and are charged differently for [AI Providers](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers). 

The pricing type (`&lt;PRICING_TYPE&gt;`) in the `pricing` object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks will change as follows for messages with a pricing category (`&lt;PRICING_CATEGORY&gt;`) of `service` or `group_service`:

| Which messages | Through Sep. 30, 2026 | Through Sep. 30, 2026 | As of Oct. 1, 2026 | As of Oct. 1, 2026 | `type` | Charged | `type` | Charged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1:1 service messages in the free tier, per business phone number | `free_customer_service` | No | `free_customer_service` | No |
| Group service messages in the free tier, per business phone number | `free_group_customer_service` | No | `free_group_customer_service` | No |
| 1:1 service messages after the free tier has been used | `free_customer_service` | No | `regular` | Yes |
| Group service messages after the free tier has been used | `free_group_customer_service` | No | `regular` | Yes |

##### Service message in the free monthly tier

For a 1:1 service message delivered while the business phone number is within its free tier:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_customer_service&quot;,
  &quot;category&quot;: &quot;service&quot;
&#125;
```

For a group service message within the free tier:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_group_customer_service&quot;,
  &quot;category&quot;: &quot;group_service&quot;
&#125;
```

##### Service message that is charged

For a 1:1 service message delivered after the business phone number&#039;s free tier has been used:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;service&quot;
&#125;
```

For a group service message delivered after the free tier has been used:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;group_service&quot;
&#125;
```

#### 3. Utility rates, effective October 1, 2026 &#123;#utility-rates-effective-october-1-2026&#125;

- _Effective October 1, 2026_ – Meta will charge for utility messages sent in an open [24-hour customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows), as [announced July 1, 2026](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages#upcoming-pricing-updates). 
- There is no change to when a utility message can be sent; businesses can leverage a utility template message to either reach out to or respond to users, thus even when there is _not_ an open customer service window.  

The pricing type (`&lt;PRICING_TYPE&gt;`) in the `pricing` object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks will change as follows for messages with a pricing category (`&lt;PRICING_CATEGORY&gt;`) of `utility` or `group_utility` that are sent in response to users, within an open customer service window:

| Which messages | Through Sep. 30, 2026 | Through Sep. 30, 2026 | As of Oct. 1, 2026 | As of Oct. 1, 2026 | `type` | Charged | `type` | Charged |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1:1 utility messages sent in response to users, so within the 24-hour customer service window | `free_customer_service` | No | `regular` | Yes |
| Group utility messages sent within an open group customer service window | `free_group_customer_service` | No | `regular` | Yes |

##### Utility message sent in response to a user

Through September 30, 2026, the `pricing` object for a 1:1 utility message sent within an open customer service window is:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_customer_service&quot;,
  &quot;category&quot;: &quot;utility&quot;
&#125;
```

For a group utility message sent within an open group customer service window through September 30, 2026:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_group_customer_service&quot;,
  &quot;category&quot;: &quot;group_utility&quot;
&#125;
```

As of October 1, 2026, the `pricing` object for a 1:1 utility message sent within an open customer service window is:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;utility&quot;
&#125;
```

For a group utility message sent within an open group customer service window as of October 1, 2026:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;group_utility&quot;
&#125;
```

#### Rate cards effective October 1, 2026

**Warning:** Below are future updates to our rates. See our [rate cards](#rate-cards-and-volume-tiers) above for current rates.

| Currency | Rates (csv) | Volume tiers (csv) | Rates and volume tiers (PDF) |
| --- | --- | --- | --- |
| USD | USD rates | USD volume tiers2 | USD rates and volume tiers1,2 |
| AED | AED rates | AED volume tiers | AED rates and volume tiers |
| ARS | ARS rates | ARS volume tiers | ARS rates and volume tiers |
| AUD | AUD rates | AUD volume tiers | AUD rates and volume tiers |
| BRL | BRL rates | BRL volume tiers | BRL rates and volume tiers |
| CLP | CLP rates | CLP volume tiers | CLP rates and volume tiers |
| COP | COP rates | COP volume tiers | COP rates and volume tiers |
| EUR | EUR rates | EUR volume tiers | EUR rates and volume tiers |
| GBP | GBP rates | GBP volume tiers | GBP rates and volume tiers |
| IDR | IDR rates | IDR volume tiers | IDR rates and volume tiers |
| INR | INR rates | INR volume tiers | INR rates and volume tiers |
| MXN | MXN rates | MXN volume tiers | MXN rates and volume tiers |
| MYR | MYR rates | MYR volume tiers | MYR rates and volume tiers |
| PEN | PEN rates | PEN volume tiers | PEN rates and volume tiers |
| SAR | SAR rates | SAR volume tiers | SAR rates and volume tiers |
| SGD | SGD rates | SGD volume tiers | SGD rates and volume tiers |

1. For USD only - The PDF contained errors for volume tiers of specific markets. This was updated as of Sep. 14, 2026. 
2. For USD only - The PDF and CSV of volume tiers contained errors for Rest of Central &amp; Eastern Europe; it showed updates to 2 of the tier rates. There is no pricing change for Oct. 1 &#039;26 for this pricing region. This was updated as of Sep. 24, 2026.

#### As announced May 27, 2026
To provide more than 1-month notice - more time to plan and prepare - Meta shared pricing updates launching October 1, 2026 by June 1, 2026. Consistent with July 1, 2026, Meta will move additional markets out of their respective &quot;Rest Of&quot; pricing region to be standalone on rate cards. Below are at least the markets Meta will move out, and the corresponding updates to rates. Meta will announce to-be rates no later than September 1, 2026, per the [pricing calendar](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#pricing-calendar).

- Bangladesh\*, Iraq\*, Nepal\*, Sri Lanka\* – Lower utility and authentication rates, plus a new authentication-international rate that is higher vs. the current regional authentication rate
- Kazakhstan\*, Kuwait\*, Morocco\*, Oman\*, Ukraine\* – Higher utility and authentication rates, plus a new authentication-international rate that is higher vs. the current regional authentication rate

### Pricing updates effective August 1, 2026 and October 1, 2026

Pricing updates for Meta Business Agent, service, and utility messages will launch on August 1, 2026 and October 1, 2026. Refer [here to learn more](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages).

### Billing localization for Brazil and India

**Brazil**

**Warning:** For Brazil, gradual roll-out began as planned on July 1, 2026. As of July 16, 2026, all eligible Solution Providers and directly-integrated businesses can create new Messaging accounts in BRL.

*Effective July 1, 2026, as of 9am PT* – Only Solution Providers and directly-integrated businesses whose Sold-To country is Brazil in [Billing Hub](https://business.facebook.com/billing_hub/legal_entities) (eligible customers) can create new Messaging accounts in BRL (Brazilian Reals). Learn more about billing localization for Brazil [here](https://www.facebook.com/business/help/4344414845795884).

Per-message rates in BRL are now published [below](#updates-to-rate-cards). Charges from any BRL Messaging account will be invoiced in BRL by Meta&#039;s local entity in Brazil, Facebook Brasil.

As a reminder, eligible customers must ensure all Messaging accounts in their business portfolio are migrated to BRL by June 30, 2027 to avoid disruptions, since as of July 1, 2027 Meta will no longer deliver the messages of non-BRL Messaging accounts of eligible customers. To make this migration process easier and faster, use the [Currency Migration API](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/change-billing-currency), which is available as of June 1, 2026.

**India**

Billing localization launched on January 1, 2026 for Solution Providers and directly-integrated businesses whose Sold-To country is India in [Billing Hub](https://business.facebook.com/billing_hub/legal_entities) (eligible customers). Learn more [here](https://www.facebook.com/business/help/2301408543603167).

Eligible customers must ensure all Messaging accounts in their business portfolio are migrated to INR by December 31, 2026 to avoid disruptions, since as of January 1, 2027 Meta will no longer deliver the messages of non-INR Messaging accounts of eligible customers. To make this migration process easier and faster, use the [Currency Migration API](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/change-billing-currency), which is available as of June 1, 2026.

### Previous rate card updates

- Effective July 1, 2026 at 12am by Messaging account timezone, the rate updates below applied:
  - Hong Kong\* – Higher utility and authentication rates.
  - Hungary\* – Higher utility and authentication rates.
  - Italy – Higher marketing message rate.
  - Poland\* – Lower marketing, utility and authentication rates.
  - Qatar\* – Higher utility and authentication rates.
  - Romania\* – Higher utility and authentication rates.
  - Singapore\* – Higher utility and authentication rates.
  - Spain – Higher marketing message rate.
  - United Kingdom – Higher marketing message rate.

  \* Until June 30, 2026, messages to users in these markets were charged the respective regional rates (e.g., Rest of Central and Eastern Europe for Poland). These markets have been moved out of regional rate pricing to be standalone on rate cards, with market-specific rates.

  For utility and authentication messages – Volume tiers for these markets are now market-specific. For example, messages businesses send to users in Poland a/ no longer count toward the volume tiers of Rest of Central and Eastern Europe and instead b/ count toward the volume tiers of Poland.

- Effective April 1, 2026 at 12am by Messaging account timezone, the rate updates below applied:
  - Saudi Arabia – Higher marketing message rate.
  - India – Higher authentication-international rate.
  - Pakistan – Higher utility and authentication rates. No change to the authentication-international rate.
  - Turkey – Lower utility and authentication rates.
  - 8 new billing currencies introduced: ARS (Argentina), CLP (Chile), COP (Colombia), MYR (Malaysia), PEN (Peru), SAR (Saudi Arabia), SGD (Singapore), AED (United Arab Emirates).

- Effective January 1, 2026 at 12am by Messaging account timezone, the rate updates below applied:
  - India - Higher marketing rate.
  - France, Egypt - Lower marketing rates.
  - North America - Lower utility and authentication rates.

- Effective October 1, 2025 at 12am by Messaging account timezone, the rate updates below applied:
  - Colombia – Higher utility and authentication rates.
  - Mexico – Lower marketing rates.
  - United Arab Emirates – Higher marketing message rate.
  - Argentina, Egypt, Saudi Arabia – Lower utility and authentication rates.
  - Zimbabwe is mapped to our &quot;Rest of Africa&quot; region vs. &quot;Other&quot;. Messages delivered to WhatsApp users with a +263 country calling code (Zimbabwe) will be charged &quot;Rest of Africa&quot; rates.

- Effective July 1, 2025 – Lower utility and authentication message rates across several markets, to ensure pricing is on-par to alternate channels for these use cases. Marketing conversation rates became marketing message rates.
- Effective April 1, 2025 – Lowered [authentication-international conversation rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates) for Egypt, Nigeria, Pakistan, and South Africa.
- Effective February 1, 2025 – Lowered [authentication conversation rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#rates) for Egypt, Malaysia, Nigeria, Pakistan, Saudi Arabia, South Africa, and the United Arab Emirates.
- Effective November 1, 2024 – [Service conversations](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/conversation-based-pricing#service-conversations) are now free for all businesses.
- Effective October 1, 2024 – Updated [marketing conversation rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#rates) in India, Saudi Arabia, the United Arab Emirates, and the United Kingdom.
- Effective August 1, 2024 – Lowered [utility conversation rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#rates).

### Authentication-international rates

Specific countries have an authentication-international rate. Our rate cards reflect these rates. See [Authentication-International rates](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/authentication-international-rates) to learn about these rates and if they apply to you.

### Country calling codes

Charges for messages are based on the country calling code of the recipient WhatsApp phone number. The table below shows how Meta maps country calling codes and ISO 3166 Alpha-2 country codes to countries or regions. If a country is not listed below, it maps to **Other**.

| Markets | Calling Code&lt;br&gt;&lt;br&gt;(and network prefix if applicable) | ISO Country Code |
| --- | --- | --- |
| Countries&lt;br&gt;&lt;br&gt;Argentina&lt;br&gt;&lt;br&gt;Brazil&lt;br&gt;&lt;br&gt;Chile&lt;br&gt;&lt;br&gt;Colombia&lt;br&gt;&lt;br&gt;Egypt&lt;br&gt;&lt;br&gt;France&lt;br&gt;&lt;br&gt;Germany&lt;br&gt;&lt;br&gt;Hong Kong&lt;br&gt;&lt;br&gt;Hungary&lt;br&gt;&lt;br&gt;India&lt;br&gt;&lt;br&gt;Indonesia&lt;br&gt;&lt;br&gt;Israel&lt;br&gt;&lt;br&gt;Italy&lt;br&gt;&lt;br&gt;Malaysia&lt;br&gt;&lt;br&gt;Mexico&lt;br&gt;&lt;br&gt;Netherlands&lt;br&gt;&lt;br&gt;Nigeria&lt;br&gt;&lt;br&gt;Pakistan&lt;br&gt;&lt;br&gt;Peru&lt;br&gt;&lt;br&gt;Poland&lt;br&gt;&lt;br&gt;Qatar&lt;br&gt;&lt;br&gt;Romania&lt;br&gt;&lt;br&gt;Russia&lt;br&gt;&lt;br&gt;Saudi Arabia&lt;br&gt;&lt;br&gt;Singapore&lt;br&gt;&lt;br&gt;South Africa&lt;br&gt;&lt;br&gt;Spain&lt;br&gt;&lt;br&gt;Turkey&lt;br&gt;&lt;br&gt;United Arab Emirates&lt;br&gt;&lt;br&gt;United Kingdom | 54&lt;br&gt;&lt;br&gt;55&lt;br&gt;&lt;br&gt;56&lt;br&gt;&lt;br&gt;57&lt;br&gt;&lt;br&gt;20&lt;br&gt;&lt;br&gt;33&lt;br&gt;&lt;br&gt;49&lt;br&gt;&lt;br&gt;852&lt;br&gt;&lt;br&gt;36&lt;br&gt;&lt;br&gt;91&lt;br&gt;&lt;br&gt;62&lt;br&gt;&lt;br&gt;972&lt;br&gt;&lt;br&gt;39&lt;br&gt;&lt;br&gt;60&lt;br&gt;&lt;br&gt;52&lt;br&gt;&lt;br&gt;31&lt;br&gt;&lt;br&gt;234&lt;br&gt;&lt;br&gt;92&lt;br&gt;&lt;br&gt;51&lt;br&gt;&lt;br&gt;48&lt;br&gt;&lt;br&gt;974&lt;br&gt;&lt;br&gt;40&lt;br&gt;&lt;br&gt;7&lt;br&gt;&lt;br&gt;966&lt;br&gt;&lt;br&gt;65&lt;br&gt;&lt;br&gt;27&lt;br&gt;&lt;br&gt;34&lt;br&gt;&lt;br&gt;90&lt;br&gt;&lt;br&gt;971&lt;br&gt;&lt;br&gt;44 | AR&lt;br&gt;&lt;br&gt;BR&lt;br&gt;&lt;br&gt;CL&lt;br&gt;&lt;br&gt;CO&lt;br&gt;&lt;br&gt;EG&lt;br&gt;&lt;br&gt;FR&lt;br&gt;&lt;br&gt;DE&lt;br&gt;&lt;br&gt;HK&lt;br&gt;&lt;br&gt;HU&lt;br&gt;&lt;br&gt;IN&lt;br&gt;&lt;br&gt;ID&lt;br&gt;&lt;br&gt;IL&lt;br&gt;&lt;br&gt;IT&lt;br&gt;&lt;br&gt;MY&lt;br&gt;&lt;br&gt;MX&lt;br&gt;&lt;br&gt;NL&lt;br&gt;&lt;br&gt;NG&lt;br&gt;&lt;br&gt;PK&lt;br&gt;&lt;br&gt;PE&lt;br&gt;&lt;br&gt;PL&lt;br&gt;&lt;br&gt;QA&lt;br&gt;&lt;br&gt;RO&lt;br&gt;&lt;br&gt;RU&lt;br&gt;&lt;br&gt;SA&lt;br&gt;&lt;br&gt;SG&lt;br&gt;&lt;br&gt;ZA&lt;br&gt;&lt;br&gt;ES&lt;br&gt;&lt;br&gt;TR&lt;br&gt;&lt;br&gt;AE&lt;br&gt;&lt;br&gt;GB |
| North America&lt;br&gt;&lt;br&gt;Canada&lt;br&gt;&lt;br&gt;United States | 1&lt;br&gt;&lt;br&gt;1 | CA&lt;br&gt;&lt;br&gt;US |
| Rest of Africa&lt;br&gt;&lt;br&gt;Algeria&lt;br&gt;&lt;br&gt;Angola&lt;br&gt;&lt;br&gt;Benin&lt;br&gt;&lt;br&gt;Botswana&lt;br&gt;&lt;br&gt;Burkina Faso&lt;br&gt;&lt;br&gt;Burundi&lt;br&gt;&lt;br&gt;Cameroon&lt;br&gt;&lt;br&gt;Chad&lt;br&gt;&lt;br&gt;Republic of the Congo (Brazzaville)&lt;br&gt;&lt;br&gt;Eritrea&lt;br&gt;&lt;br&gt;Ethiopia&lt;br&gt;&lt;br&gt;Gabon&lt;br&gt;&lt;br&gt;Gambia&lt;br&gt;&lt;br&gt;Ghana&lt;br&gt;&lt;br&gt;Guinea-Bissau&lt;br&gt;&lt;br&gt;Ivory Coast&lt;br&gt;&lt;br&gt;Kenya&lt;br&gt;&lt;br&gt;Lesotho&lt;br&gt;&lt;br&gt;Liberia&lt;br&gt;&lt;br&gt;Libya&lt;br&gt;&lt;br&gt;Madagascar&lt;br&gt;&lt;br&gt;Malawi&lt;br&gt;&lt;br&gt;Mali&lt;br&gt;&lt;br&gt;Mauritania&lt;br&gt;&lt;br&gt;Morocco&lt;br&gt;&lt;br&gt;Mozambique&lt;br&gt;&lt;br&gt;Namibia&lt;br&gt;&lt;br&gt;Niger&lt;br&gt;&lt;br&gt;Rwanda&lt;br&gt;&lt;br&gt;Senegal&lt;br&gt;&lt;br&gt;Sierra Leone&lt;br&gt;&lt;br&gt;Somalia&lt;br&gt;&lt;br&gt;South Sudan&lt;br&gt;&lt;br&gt;Sudan&lt;br&gt;&lt;br&gt;Swaziland&lt;br&gt;&lt;br&gt;Tanzania&lt;br&gt;&lt;br&gt;Togo&lt;br&gt;&lt;br&gt;Tunisia&lt;br&gt;&lt;br&gt;Uganda&lt;br&gt;&lt;br&gt;Zambia&lt;br&gt;&lt;br&gt;Zimbabwe | 213&lt;br&gt;&lt;br&gt;244&lt;br&gt;&lt;br&gt;229&lt;br&gt;&lt;br&gt;267&lt;br&gt;&lt;br&gt;226&lt;br&gt;&lt;br&gt;257&lt;br&gt;&lt;br&gt;237&lt;br&gt;&lt;br&gt;235&lt;br&gt;&lt;br&gt;242&lt;br&gt;&lt;br&gt;291&lt;br&gt;&lt;br&gt;251&lt;br&gt;&lt;br&gt;241&lt;br&gt;&lt;br&gt;220&lt;br&gt;&lt;br&gt;233&lt;br&gt;&lt;br&gt;245&lt;br&gt;&lt;br&gt;225&lt;br&gt;&lt;br&gt;254&lt;br&gt;&lt;br&gt;266&lt;br&gt;&lt;br&gt;231&lt;br&gt;&lt;br&gt;218&lt;br&gt;&lt;br&gt;261&lt;br&gt;&lt;br&gt;265&lt;br&gt;&lt;br&gt;223&lt;br&gt;&lt;br&gt;222&lt;br&gt;&lt;br&gt;212&lt;br&gt;&lt;br&gt;258&lt;br&gt;&lt;br&gt;264&lt;br&gt;&lt;br&gt;227&lt;br&gt;&lt;br&gt;250&lt;br&gt;&lt;br&gt;221&lt;br&gt;&lt;br&gt;232&lt;br&gt;&lt;br&gt;252&lt;br&gt;&lt;br&gt;211&lt;br&gt;&lt;br&gt;249&lt;br&gt;&lt;br&gt;268&lt;br&gt;&lt;br&gt;255&lt;br&gt;&lt;br&gt;228&lt;br&gt;&lt;br&gt;216&lt;br&gt;&lt;br&gt;256&lt;br&gt;&lt;br&gt;260&lt;br&gt;&lt;br&gt;263 | DZ&lt;br&gt;&lt;br&gt;AO&lt;br&gt;&lt;br&gt;BJ&lt;br&gt;&lt;br&gt;BW&lt;br&gt;&lt;br&gt;BF&lt;br&gt;&lt;br&gt;BI&lt;br&gt;&lt;br&gt;CM&lt;br&gt;&lt;br&gt;TD&lt;br&gt;&lt;br&gt;CG&lt;br&gt;&lt;br&gt;ER&lt;br&gt;&lt;br&gt;ET&lt;br&gt;&lt;br&gt;GA&lt;br&gt;&lt;br&gt;GM&lt;br&gt;&lt;br&gt;GH&lt;br&gt;&lt;br&gt;GW&lt;br&gt;&lt;br&gt;CI&lt;br&gt;&lt;br&gt;KE&lt;br&gt;&lt;br&gt;LS&lt;br&gt;&lt;br&gt;LR&lt;br&gt;&lt;br&gt;LY&lt;br&gt;&lt;br&gt;MG&lt;br&gt;&lt;br&gt;MW&lt;br&gt;&lt;br&gt;ML&lt;br&gt;&lt;br&gt;MR&lt;br&gt;&lt;br&gt;MA&lt;br&gt;&lt;br&gt;MZ&lt;br&gt;&lt;br&gt;NA&lt;br&gt;&lt;br&gt;NE&lt;br&gt;&lt;br&gt;RW&lt;br&gt;&lt;br&gt;SN&lt;br&gt;&lt;br&gt;SL&lt;br&gt;&lt;br&gt;SO&lt;br&gt;&lt;br&gt;SS&lt;br&gt;&lt;br&gt;SD&lt;br&gt;&lt;br&gt;SZ&lt;br&gt;&lt;br&gt;TZ&lt;br&gt;&lt;br&gt;TG&lt;br&gt;&lt;br&gt;TN&lt;br&gt;&lt;br&gt;UG&lt;br&gt;&lt;br&gt;ZM&lt;br&gt;&lt;br&gt;ZW |
| Rest of Asia Pacific&lt;br&gt;&lt;br&gt;Afghanistan&lt;br&gt;&lt;br&gt;Australia&lt;br&gt;&lt;br&gt;Bangladesh&lt;br&gt;&lt;br&gt;Cambodia&lt;br&gt;&lt;br&gt;China&lt;br&gt;&lt;br&gt;Japan&lt;br&gt;&lt;br&gt;Laos&lt;br&gt;&lt;br&gt;Mongolia&lt;br&gt;&lt;br&gt;Nepal&lt;br&gt;&lt;br&gt;New Zealand&lt;br&gt;&lt;br&gt;Papua New Guinea&lt;br&gt;&lt;br&gt;Philippines&lt;br&gt;&lt;br&gt;Sri Lanka&lt;br&gt;&lt;br&gt;Taiwan&lt;br&gt;&lt;br&gt;Tajikistan&lt;br&gt;&lt;br&gt;Thailand&lt;br&gt;&lt;br&gt;Turkmenistan&lt;br&gt;&lt;br&gt;Uzbekistan&lt;br&gt;&lt;br&gt;Vietnam | 93&lt;br&gt;&lt;br&gt;61&lt;br&gt;&lt;br&gt;880&lt;br&gt;&lt;br&gt;855&lt;br&gt;&lt;br&gt;86&lt;br&gt;&lt;br&gt;81&lt;br&gt;&lt;br&gt;856&lt;br&gt;&lt;br&gt;976&lt;br&gt;&lt;br&gt;977&lt;br&gt;&lt;br&gt;64&lt;br&gt;&lt;br&gt;675&lt;br&gt;&lt;br&gt;63&lt;br&gt;&lt;br&gt;94&lt;br&gt;&lt;br&gt;886&lt;br&gt;&lt;br&gt;992&lt;br&gt;&lt;br&gt;66&lt;br&gt;&lt;br&gt;993&lt;br&gt;&lt;br&gt;998&lt;br&gt;&lt;br&gt;84 | AF&lt;br&gt;&lt;br&gt;AU&lt;br&gt;&lt;br&gt;BD&lt;br&gt;&lt;br&gt;KH&lt;br&gt;&lt;br&gt;CN&lt;br&gt;&lt;br&gt;JP&lt;br&gt;&lt;br&gt;LA&lt;br&gt;&lt;br&gt;MN&lt;br&gt;&lt;br&gt;NP&lt;br&gt;&lt;br&gt;NZ&lt;br&gt;&lt;br&gt;PG&lt;br&gt;&lt;br&gt;PH&lt;br&gt;&lt;br&gt;LK&lt;br&gt;&lt;br&gt;TW&lt;br&gt;&lt;br&gt;TJ&lt;br&gt;&lt;br&gt;TH&lt;br&gt;&lt;br&gt;TM&lt;br&gt;&lt;br&gt;UZ&lt;br&gt;&lt;br&gt;VN |
| Rest of Central and Eastern Europe&lt;br&gt;&lt;br&gt;Albania&lt;br&gt;&lt;br&gt;Armenia&lt;br&gt;&lt;br&gt;Azerbaijan&lt;br&gt;&lt;br&gt;Belarus&lt;br&gt;&lt;br&gt;Bulgaria&lt;br&gt;&lt;br&gt;Croatia&lt;br&gt;&lt;br&gt;Czech Republic&lt;br&gt;&lt;br&gt;Georgia&lt;br&gt;&lt;br&gt;Greece&lt;br&gt;&lt;br&gt;Latvia&lt;br&gt;&lt;br&gt;Lithuania&lt;br&gt;&lt;br&gt;Moldova&lt;br&gt;&lt;br&gt;North Macedonia&lt;br&gt;&lt;br&gt;Serbia&lt;br&gt;&lt;br&gt;Slovakia&lt;br&gt;&lt;br&gt;Slovenia&lt;br&gt;&lt;br&gt;Ukraine | 355&lt;br&gt;&lt;br&gt;374&lt;br&gt;&lt;br&gt;994&lt;br&gt;&lt;br&gt;375&lt;br&gt;&lt;br&gt;359&lt;br&gt;&lt;br&gt;385&lt;br&gt;&lt;br&gt;420&lt;br&gt;&lt;br&gt;995&lt;br&gt;&lt;br&gt;30&lt;br&gt;&lt;br&gt;371&lt;br&gt;&lt;br&gt;370&lt;br&gt;&lt;br&gt;373&lt;br&gt;&lt;br&gt;389&lt;br&gt;&lt;br&gt;381&lt;br&gt;&lt;br&gt;421&lt;br&gt;&lt;br&gt;386&lt;br&gt;&lt;br&gt;380 | AL&lt;br&gt;&lt;br&gt;AM&lt;br&gt;&lt;br&gt;AZ&lt;br&gt;&lt;br&gt;BY&lt;br&gt;&lt;br&gt;BG&lt;br&gt;&lt;br&gt;HR&lt;br&gt;&lt;br&gt;CZ&lt;br&gt;&lt;br&gt;GE&lt;br&gt;&lt;br&gt;GR&lt;br&gt;&lt;br&gt;LV&lt;br&gt;&lt;br&gt;LT&lt;br&gt;&lt;br&gt;MD&lt;br&gt;&lt;br&gt;MK&lt;br&gt;&lt;br&gt;RS&lt;br&gt;&lt;br&gt;SK&lt;br&gt;&lt;br&gt;SI&lt;br&gt;&lt;br&gt;UA |
| Rest of Western Europe&lt;br&gt;&lt;br&gt;Austria&lt;br&gt;&lt;br&gt;Belgium&lt;br&gt;&lt;br&gt;Denmark&lt;br&gt;&lt;br&gt;Finland&lt;br&gt;&lt;br&gt;Ireland&lt;br&gt;&lt;br&gt;Norway&lt;br&gt;&lt;br&gt;Portugal&lt;br&gt;&lt;br&gt;Sweden&lt;br&gt;&lt;br&gt;Switzerland | 43&lt;br&gt;&lt;br&gt;32&lt;br&gt;&lt;br&gt;45&lt;br&gt;&lt;br&gt;358&lt;br&gt;&lt;br&gt;353&lt;br&gt;&lt;br&gt;47&lt;br&gt;&lt;br&gt;351&lt;br&gt;&lt;br&gt;46&lt;br&gt;&lt;br&gt;41 | AT&lt;br&gt;&lt;br&gt;BE&lt;br&gt;&lt;br&gt;DK&lt;br&gt;&lt;br&gt;FI&lt;br&gt;&lt;br&gt;IE&lt;br&gt;&lt;br&gt;NO&lt;br&gt;&lt;br&gt;PT&lt;br&gt;&lt;br&gt;SE&lt;br&gt;&lt;br&gt;CH |
| Rest of Latin America&lt;br&gt;&lt;br&gt;Bolivia&lt;br&gt;&lt;br&gt;Costa Rica&lt;br&gt;&lt;br&gt;Dominican Republic&lt;br&gt;&lt;br&gt;Ecuador&lt;br&gt;&lt;br&gt;El Salvador&lt;br&gt;&lt;br&gt;Guatemala&lt;br&gt;&lt;br&gt;Haiti&lt;br&gt;&lt;br&gt;Honduras&lt;br&gt;&lt;br&gt;Jamaica&lt;br&gt;&lt;br&gt;Nicaragua&lt;br&gt;&lt;br&gt;Panama&lt;br&gt;&lt;br&gt;Paraguay&lt;br&gt;&lt;br&gt;Puerto Rico&lt;br&gt;&lt;br&gt;Uruguay&lt;br&gt;&lt;br&gt;Venezuela | 591&lt;br&gt;&lt;br&gt;506&lt;br&gt;&lt;br&gt;1 (809, 829, 849)&lt;br&gt;&lt;br&gt;593&lt;br&gt;&lt;br&gt;503&lt;br&gt;&lt;br&gt;502&lt;br&gt;&lt;br&gt;509&lt;br&gt;&lt;br&gt;504&lt;br&gt;&lt;br&gt;1 (658, 876)&lt;br&gt;&lt;br&gt;505&lt;br&gt;&lt;br&gt;507&lt;br&gt;&lt;br&gt;595&lt;br&gt;&lt;br&gt;1 (787, 939)&lt;br&gt;&lt;br&gt;598&lt;br&gt;&lt;br&gt;58 | BO&lt;br&gt;&lt;br&gt;CR&lt;br&gt;&lt;br&gt;DO&lt;br&gt;&lt;br&gt;EC&lt;br&gt;&lt;br&gt;SV&lt;br&gt;&lt;br&gt;GT&lt;br&gt;&lt;br&gt;HT&lt;br&gt;&lt;br&gt;HN&lt;br&gt;&lt;br&gt;JM&lt;br&gt;&lt;br&gt;NI&lt;br&gt;&lt;br&gt;PA&lt;br&gt;&lt;br&gt;PY&lt;br&gt;&lt;br&gt;PR&lt;br&gt;&lt;br&gt;UY&lt;br&gt;&lt;br&gt;VE |
| Rest of Middle East&lt;br&gt;&lt;br&gt;Bahrain&lt;br&gt;&lt;br&gt;Iraq&lt;br&gt;&lt;br&gt;Jordan&lt;br&gt;&lt;br&gt;Kuwait&lt;br&gt;&lt;br&gt;Lebanon&lt;br&gt;&lt;br&gt;Oman&lt;br&gt;&lt;br&gt;Yemen | 973&lt;br&gt;&lt;br&gt;964&lt;br&gt;&lt;br&gt;962&lt;br&gt;&lt;br&gt;965&lt;br&gt;&lt;br&gt;961&lt;br&gt;&lt;br&gt;968&lt;br&gt;&lt;br&gt;967 | BH&lt;br&gt;&lt;br&gt;IQ&lt;br&gt;&lt;br&gt;JO&lt;br&gt;&lt;br&gt;KW&lt;br&gt;&lt;br&gt;LB&lt;br&gt;&lt;br&gt;OM&lt;br&gt;&lt;br&gt;YE |
| Other&lt;br&gt;&lt;br&gt;All other countries | Varies by country |  |

## Volume tiers

You can unlock lower utility and authentication rates based on the number of messages you send in a month.

### Tiering accrual

- **Messages are aggregated at the business portfolio level, across all Messaging accounts owned by the portfolio** — To determine what tier rates may apply in a given month for a given market–category pair, Meta aggregates messages across all of a business portfolio&#039;s Messaging accounts for each market-category pair (for example, Brazil–authentication, Brazil–utility, India–authentication, and so on).
- **Only messages that are charged count toward the tiers** — Thus, the following messages do not count:
  - Utility templates delivered to WhatsApp users within an open customer service window.
   - Utility templates delivered within a [free entry point window](#free-entry-point-windows).
- **Volume tiers will be determined solely by Meta** — All insights data is approximate due to small variations in data processing. Undue reliance should not be placed on insights data.

### Key dynamics

- **Tiers are market–category specific** — Volume tiers are aligned to our rate cards and differ by market (e.g., Brazil or Rest of Latin America) and category (utility, authentication).
- **Rates are tier-specific** — When a business sends enough messages at a given market–category pair to reach the next tier, they unlock the rate of the next tier, specifically for messages in that tier. This rate applies across all of their Messaging accounts.
- **Tiers reset monthly** — At the start of the next month (12am Messaging account timezone), message count resets to 0 and businesses begin to accrue messages toward that month.

### Volume tiers examples

The table below is illustrative and only highlights the dynamics of volume tiers. Please refer to our [rate cards](#rate-cards-and-volume-tiers) to see the rates charged.

Below are several examples to highlight how the tiers work and what is charged in a given month, for a given market–category. These examples refer to the illustrative table above:

Example 1: A business that sends a total of B authentication messages in a month to India is charged:

- List rate for the first A messages.
- Tier rate 1 for messages A+1 to B.
- Total charges for that month = Rate per tier 𝗑 messages in each tier.

Example 2: A business that starts to be charged our authentication-international rates on the 15th day of the month:

- Day 1 to 14 of that month: Volume tiers apply on the authentication rate.
- Day 15 onward of that month: Volume tiers apply on the authentication-international rate, with messages continuing to accrue in that month. For example, if a business has already reached the Tier 2, the business would be charged Tier 2&#039;s authentication-international rate:

Example 3: A business has 3 Messaging accounts sending authentication messages to India. For Messaging account A, it is still July 31 based on their timezone. For Messaging accounts B and C, it is already August 1 based on their timezone. For July, the business is already being charged Tier Rate 1.

- The business portfolio will be accruing toward tiers for both July (via Messaging account A) and August (via Messaging accounts B, C) for a period of time.
- The business can reach the next tier for July, via Messaging account A. If that happens, messages for the remainder of July for Messaging account A will be charged Tier Rate 2.

Example 4: A business has 3 Messaging accounts, integrated across 2 partners. Provider 1 sends the first B messages in a given month, and provider 2 starts sending messages as of when the business is in the 3rd tier. The business does not send enough messages that month to reach the next tier. What Meta charges each provider:

- Provider 1: List rate for A messages, then Tier Rate 1 from A+1 to B, and Tier Rate 2 for B+1 to C.
- Provider 2: Tier Rate 2 across all of their messages.

### Tiering webhooks

Starting October 1, 2025, an [account_update](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/account_update) webhook with `event` set to `VOLUME_BASED_PRICING_TIER_UPDATE` will be triggered when your Messaging account reaches a new volume tier, in any market, in a given month. This complements our [pricing_analytics](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics) endpoint, which will continue to provide intra-month tiering progress and tiering information for delivered messages.

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

Note that it&#039;s possible for multiple [account_update](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/account_update) webhooks to be triggered that describe the same tier switch event. In these cases, use the webhook with the smaller `tier_update_time` Unix timestamp as the official webhook.

### Tiering analytics

You can get [volume tier information](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#volume-tier-information) via [template analytics](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#template-analytics).

## When messages are not charged
Meta does not charge for messages in certain cases, as outlined below.

### Non-template messages

**Warning:** Pricing updates for Meta Business Agent, service, and utility messages will launch on August 1, 2026 and October 1, 2026. [Learn more](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages).

Non-template messages, which can only be sent within an open [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows), are not charged as of November 1, 2024. These messages  have `type` set to `free_customer_service` in the `pricing` object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_customer_service&quot;,
  &quot;category&quot;: &quot;service&quot;
&#125;
```

### Customer service windows with multiple Messaging accounts

A customer service window is tracked at the business phone number level, for each business phone number and WhatsApp user pair. It is not scoped to a Messaging account.

When several Messaging accounts send on the same business phone number, they all share the same customer service window with a given WhatsApp user:

- Any Messaging account sending on that phone number can send free non-template messages while the window is open.
- Free utility template delivery within an open window applies to any Messaging account sending on that phone number.
- Handing a conversation between partners does not open a separate window, because the window follows the phone number rather than the Messaging account.

### Utility template messages in response to users

**Warning:** Pricing updates for Meta Business Agent, service, and utility messages will launch on August 1, 2026 and October 1, 2026. [Learn more](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages).

Utility template messages sent within an open [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows) are not charged as of July 1, 2025. These messages will have `type` set to `free_customer_service` and `category` set to `utility` in the `pricing` object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks:

```json
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: false,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;free_customer_service&quot;,
  &quot;category&quot;: &quot;utility&quot;
&#125;
```

#### Edge case

If you send a message to a WhatsApp user prior to July 1, 2025 (which is when Meta switched from conversation-based pricing to per-message pricing), a utility conversation is opened between you and a user that spans the switch to per-message pricing (the conversation was opened before the switch but won&#039;t close until after the switch). In this case, utility templates sent to the user after the switch while the conversation is open will be free, but attributed to the open conversation. In status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks, these messages will have a `pricing_model` of `CBP` and the utility conversation ID will be assigned to `conversation.id`. Once the conversation closes, subsequent utility messages will use per-message pricing, which will be reflected in new webhooks.

### Free entry point windows (FEP)

If a WhatsApp user messages you via an ad that clicks to WhatsApp using a device running our Android or iOS app (our desktop and web apps are not supported):

- A [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows) is opened.
- If you respond within the customer service window using any type of message, the message will be free, and a Free Entry Point (&quot;FEP&quot;) window will be opened, starting from the time when you responded.
- FEP windows may remain open for up to 7 days. While open, you can send any type of message to the user at no charge.

#### Free entry point windows with multiple Messaging accounts

Like customer service windows, a free entry point window is tracked for the business and WhatsApp user pair, not for an individual Messaging account.

When several Messaging accounts send on the same business phone number, they all share the same FEP window:

- Any Messaging account sending on that phone number can send free messages while the FEP window is open.
- The Messaging account that funded the Click to WhatsApp ad does not get exclusive use of the window.
- If a different Messaging account responds to the WhatsApp user than the one that funded the ad, messages are still free while the window is open.

## Other pricing topics

### Marketing - Max-price feature for Marketing Messages API for WhatsApp

Starting in 2026, businesses integrated into Marketing Messages API for WhatsApp can choose to set a [max-price](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/pricing) per marketing message delivery; when a max-price is set, Meta will charge that max-price or lower for delivery.

### Service - Pricing policy for AI Providers using the WhatsApp Business Platform

See the [AI Providers pricing policy](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers), effective February 16, 2026 and updated as of May 12, 2026. Pricing updates for service messages launching October 1, 2026 do **not** apply to AI Providers; see the [AI Providers pricing policy](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/ai-providers) for how Meta charges them for service messages. 

### Service - Pricing policy for eligible governments and non-profits using the WhatsApp Business Platform &#123;#service-pricing-policy-for-eligible-governments-and-non-profits&#125;

Starting October 1, 2026 - Service messages remain free beyond the monthly free tier only for eligible government and non-profit organizations using the WhatsApp Business Platform. This pricing policy will be in effect through December 31, 2027. 

Meta continues to support governments and non-profit organizations, and this update allows Meta to enable eligible governments and non-profits to maintain an always-on presence on WhatsApp, to respond to and engage with WhatsApp users. Eligible cohorts include: 
- Government departments and agencies; inter-governmental organizations 
- Community non-profit organizations, including those in public health, crisis response, disaster relief and non-partisan civic engagement 

For organizations Meta has already identified as eligible, this policy will apply as of 12am by WhatsApp Business account timezone on October 1, 2026. In parallel, Meta is investing to build programmatic ways for Solution Providers and/or these organizations to a/ understand if they are eligible and b/ request a review of their eligibility to Meta. Meta will provide an update once these are available. 


### WhatsApp Business Calling API pricing

The WhatsApp Business Calling API has different pricing. See our [Calling API pricing document](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/pricing) to learn more.

### Conversation-based pricing

[Conversation-based pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/conversation-based-pricing) is deprecated. It was replaced with per-message pricing on July 1, 2025.

## Analytics

Use the [pricing_analytics field](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics) to get per-message pricing breakdowns and tiering information for delivered messages.

## Webhooks

Billable messages have `type` set to `regular` in the `pricing` object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks:

```html
&quot;pricing&quot;: &#123;
  &quot;billable&quot;: true,
  &quot;pricing_model&quot;: &quot;PMP&quot;,
  &quot;type&quot;: &quot;regular&quot;,
  &quot;category&quot;: &quot;&lt;PRICING_CATEGORY&gt;&quot;
&#125;
```

The `&lt;PRICING_CATEGORY&gt;` tells you what rate was applied (for example, `marketing`). See the status messages webhook reference for a list of possible values.

Note that currently, tiering information is not included in any webhooks. Use the [pricing_analytics field](https://developers.facebook.com/documentation/business-messaging/whatsapp/analytics#pricing-analytics) to get tiering information for delivered messages.

## Billing

Billing and billing-related actions are handled through the Meta Business Suite. See [About Billing For Your WhatsApp Business Account](https://www.facebook.com/business/help/2225184664363779) for more information.


---

Full documentation index for this product: https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt
