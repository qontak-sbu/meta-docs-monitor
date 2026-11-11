# New pricing policy for AI Providers leveraging the WhatsApp Business Platform


**Warning:** This page is specific to &quot;AI Providers&quot; using the WhatsApp Business Platform. This does NOT change how Meta charges all other businesses using the WhatsApp Business Platform. Refer to the [pricing page](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing) for more detail.

### What messages this applies to
This is specific to service messages (`&lt;PRICING_CATEGORY&gt;` : `service`) only. Meta [resumed charging](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#effective-october-1-2026) for these messages on a per-message basis as of October 1, 2026 for all businesses using the WhatsApp Business Platform. 

### Who this applies to
The pricing policy outlined on this page is specific to &quot;AI Providers&quot; using the WhatsApp Business Platform, as defined in our [Terms of Service](https://www.whatsapp.com/legal/business-solution-terms/) updated on January 15, 2026: Providers and developers of artificial intelligence or machine learning technologies, such as large language models, generative artificial intelligence platforms, general-purpose artificial intelligence assistants, or similar technologies who provide certain services on WhatsApp Business Platform.

This does **NOT** change:
- How or what Meta charges all other businesses using the WhatsApp Business Platform. Refer to our [pricing page](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing).
- The dynamics of the [customer service window](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/send-messages#customer-service-windows); service messages can still only be sent in response to users, during an open 24-hour customer service window.

### Why Meta is charging
*Specifically for third-party AI Providers:*

* Effective January 15, 2026, WhatsApp&#039;s [Terms of Service update](https://www.whatsapp.com/legal/business-solution-terms/) &quot;AI Providers&quot; are only permitted to offer general-purpose AI assistants on the WhatsApp Business Platform where Meta is legally required to permit this use case.
* Effective February 16, 2026, in countries where Meta is legally required to support AI Providers&#039; usage of the WhatsApp Business Platform, Meta will charge AI Providers for service messages delivered to WhatsApp users in these markets, as outlined below.


### What and where Meta will charge

**Warning:** This was updated on October 15, 2026 to reflect an update for Türkiye as outlined below.

This policy took effect February 16, 2026 and applies to markets as outlined below. Charges are for:
* Each service message (`&lt;PRICING_CATEGORY&gt;` : `service`)
* Delivered from an &quot;AI Provider&quot;
* To a user in a market where Meta is legally required to permit AI Providers to use the WhatsApp Business Platform

#### Markets and effective dates

Effective **October 15, 2026**
- Türkiye (+90) - AI Providers can send service messages to users in this market. Meta does not charge for these messages.

Effective **March 11, 2026**
- Brazil (+55) - AI Providers can send service messages to users in this market. Meta charges per the rates published below. 

Effective **March 11, 2026**
- AI Providers can send service messages to users in this market. From **March 11, 2026 to May 12, 2026** Meta charged per the rates published below. Meta does not charge as of May 13, 2026.
  - Austria (+43)
  - Belgium (+32)
  - Bulgaria (+359)
  - Croatia (+385)
  - Cyprus (+357)
  - Czech Republic (+420)
  - Denmark (+45)
  - Estonia (+372)
  - Finland (+358)
  - France (+33)
  - Germany (+49)
  - Greece (+30)
  - Hungary (+36)
  - Iceland (+354)
  - Ireland (+353)
  - Latvia (+371)
  - Liechtenstein (+423)
  - Lithuania (+370)
  - Luxembourg (+352)
  - Malta (+356)
  - Netherlands (+31)
  - Norway (+47)
  - Poland (+48)
  - Portugal (+351)
  - Romania (+40)
  - Slovakia (+421)
  - Slovenia (+386)
  - Spain (+34)
  - Sweden (+46)

Effective **February 16, 2026**
- Italy (+39) - AI Providers can send service messages to users in this market. From **February 16, 2026 to May 12, 2026**, Meta charged per the rates published below. Meta does not charge as of May 13, 2026.

Three examples: If a user in the respective market sends an AI Provider a prompt, and the AI provider delivers three (3) service messages in response to the user over a span of 5 minutes, that would incur... 
- Italy (+39) - Three (3) charges from Feb. 16, 2026 to May 12, 2026. No charge as of May 13, 2026. 
- Brazil (+55) - Three charges as of Mar. 11, 2026. 
- Türkiye (+90) - No charge as of Oct. 15, 2026.


### Rates

| Rates (CSV) | Rates (PDF) |
| --- | --- |
| AI Provider rates for service messages - CSV (updated Oct. 15, 2026) | AI Provider rates for service messages - PDF (updated Oct. 15, 2026) |

**Warning:** *These rates are specific to &quot;AI Providers&quot; using the WhatsApp Business Platform. These rates do NOT apply to any other businesses using the WhatsApp Business Platform. Refer to the [pricing page](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing) for more detail.*

### Analytics

The Pricing Analytics API will include a new `&lt;PRICING_CATEGORY&gt;` value of `AI_BOT` to reflect AI Provider traffic.

```
&#123;
  &quot;start&quot;: &lt;START_TIMESTAMP&gt;,
  &quot;end&quot;: &lt;END_TIMESTAMP&gt;,
  &quot;phone_number&quot;: &quot;&lt;BUSINESS_PHONE_NUMBER&gt;&quot;,
  &quot;country&quot;: &quot;&lt;COUNTRY_CODE&gt;&quot;,
  &quot;pricing_type&quot;: &quot;REGULAR&quot;,
  &quot;pricing_category&quot;: &quot;AI_BOT&quot;,
  &quot;volume&quot;: &lt;VOLUME&gt;,
  &quot;cost&quot;: &lt;COST&gt;
&#125;
```


### Webhooks


The [webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#webhooks) will reflect the `&lt;PRICING_CATEGORY&gt;` for these non-template messages from &quot;AI Providers&quot; as `general_purpose_ai`.


Billable messages have `type` set to `regular` in the pricing object of status [messages](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks/reference/messages/status) webhooks:


```
&quot;pricing&quot;: &#123;
 &quot;billable&quot;: true,
 &quot;pricing_model&quot;: &quot;PMP&quot;,
 &quot;type&quot;: &quot;regular&quot;,
 &quot;category&quot;: &quot;general_purpose_ai&quot;
&#125;
```


---

Full documentation index for this product: https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt
