# Change billing currency via API



The Currency Migration API allows you to change the billing currency or payment method by creating a new Messaging account on the same WhatsApp account hierarchy and automatically migrating your message templates, along with any Flows those templates use. Your business phone numbers are not migrated — they belong to the WhatsApp account hierarchy, which does not change.

&gt; **Important:** Only Flows used by your templates are migrated. Flows that are not used by any template are **not** migrated.

Use this API when you need to:

- **Change currency**: Clone an existing Messaging account into a new Messaging account with a different currency, migrating templates and the Flows they use. This can make it easier for you to opt-in to be charged in a [newly-available currency](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing#updates-to-rate-cards), like Mexican pesos (available as of January 1, 2026).
- **Change payment method**: Move a Messaging account from one payment method to another while preserving assets.

Under the new account model, a business can hold a separate Messaging account per billing currency on a single business phone number. When the access token you are sending with has messaging access to more than one Messaging account on a phone number, include `messaging_account_id` on your Messages API calls to name the Messaging account to bill. See [Managing messaging accounts](https://developers.facebook.com/documentation/business-messaging/whatsapp/account-model-evolution/messaging/).

## Before you begin

- The second call makes the new Messaging account the billing account and deprecates the old one. Plan for any operational timing requirements.
- Your business phone numbers stay where they are. They belong to the WhatsApp account hierarchy, and the new Messaging account is linked to that same hierarchy, so nothing about the numbers changes.
- Coexistence and Authorized Agents Messaging accounts are not eligible for migration via this API.
- **Flows not used by a template are not migrated.** Only Flows referenced by a template&#039;s Flow button are migrated.
- Both **Line of Credit** and **credit card** are supported as payment methods. The difference is only in *how* the payment method is attached to the cloned Messaging account:
  - **Line of Credit:** Pass the `EXTENDED_CREDIT_ID` in the [Set Payment Method Migration Intent](#initiate-migration) request and it is attached automatically.
  - **Credit card:** Credit cards **cannot** be attached through the API (this requires cardholder verification). After initiating the migration and **before** the [Complete migration](#complete-migration) step, you must add the payment method **manually** in your Business Manager on the newly cloned Messaging account.
  - **Important:** Regardless of type, the cloned Messaging account must have a payment method (Line of Credit or credit card) attached **before** you call **Complete migration**. If neither is attached, the migration will not complete.
- You are billed in your Messaging account&#039;s currency. Your Messaging account&#039;s currency and your legal entity&#039;s headquarters address together determine which Meta billing entity issues your invoices.
- Phone number limits are unaffected. They apply to the WhatsApp account hierarchy, which the migration does not touch.

| API Call | What is migrated | What is not migrated | Result | Can the Messaging account be used to send messages? |
| --- | --- | --- | --- | --- |
| First call (Initiate) | - Templates (all statuses: Approved, Pending, Disabled, Rejected, Under Review)&lt;br&gt;- Flows, **only** if used by a migrated template (Flow button)&lt;br&gt;- App installation&lt;br&gt;- Users/permissions | - Templates with outdated formats&lt;br&gt;- Flows not used by any template&lt;br&gt;- Insights/analytics | New Messaging account in selected currency, with assets migrated | Not yet – it is not the billing account |
| Second call (Complete) | Billing | Historical insights (remain on the old Messaging account) | The new Messaging account is the billing account for the business phone numbers on the WhatsApp account hierarchy | Yes |

| Insights | Before Migration | After Migration |
| --- | --- | --- |
| Phone Insights | Available on the old Messaging account | Historical data remains on the old Messaging account. New data appears on the new Messaging account after migration. |
| Template Insights | Available on the old Messaging account | Historical data remains on the old Messaging account. New template analytics appear on the new Messaging account. |
| Message Insights (send, delivery) | Available on the old Messaging account | Historical data remains on the old Messaging account. New message data appears on the new Messaging account. |
| Pricing Insights (cost, volume) | Available on the old Messaging account | Historical cost and volume data remains on the old Messaging account. New billing data appears on the new Messaging account in the new currency. |
| Call Insights (cost, duration, count) | Available on the old Messaging account | Historical call data remains on the old Messaging account. New call data appears on the new Messaging account. |

### Template migration behavior

During migration, note the following behavior:

- New templates created on the old Messaging account after the migration begins will not be cloned to the new Messaging account.
- Template status and category are locked during the migration process. Once migration is complete, both can change again.

### Prerequisites

Before initiating a migration, ensure the following:

- You have admin access to the source Messaging account.
- You have a valid access token with `whatsapp_business_management` and `whatsapp_business_messaging` permissions. No additional Business Portfolio Admin permissions or business approvals are required.
- If your migration requires Line of Credit billing, have your Line of Credit (also called a CreditLine) identifier ready to provide during the [Complete migration](#complete-migration) step. Lines of Credit are always denominated in USD, so you do not need one in the target currency.

## Initiate migration

Use the POST /&lt;WHATSAPP_BUSINESS_ACCOUNT_ID&gt;/`set_payment_method_migration_intent` endpoint to initiate the migration process. This validates the source Messaging account, creates a cloned Messaging account, and begins migrating assets such as templates and the Flows they use.

**Request syntax**

```html
curl -X POST &quot;https://graph.facebook.com/&lt;API_VERSION&gt;/&lt;WHATSAPP_BUSINESS_ACCOUNT_ID&gt;/set_payment_method_migration_intent&quot; \
-H &quot;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&quot; \
-H &quot;Content-Type: application/json&quot; \
-d &#039;
&#123;
  &quot;currency&quot;: &quot;&lt;CURRENCY&gt;&quot;,

  &lt;!-- Optional --&gt;
  &quot;extended_credit_id&quot;: &quot;&lt;EXTENDED_CREDIT_ID&gt;&quot;
&#125;&#039;
```

**Response syntax**

```json
&#123;
  &quot;migration_id&quot;: &quot;&lt;MIGRATION_ID&gt;&quot;,
  &quot;migration_status&quot;: &quot;&lt;MIGRATION_STATUS&gt;&quot;
&#125;
```

### Request parameters

| Placeholder | Description | Example Value |
| --- | --- | --- |
| `&lt;WHATSAPP_BUSINESS_ACCOUNT_ID&gt;` | The source Messaging account ID you are initiating migration from. Used in the endpoint path. | `123456789012345` |
| `&lt;ACCESS_TOKEN&gt;` | Access token with permissions to manage the Messaging account and perform migration actions. Used in the Authorization header. | `EAABsbCS1iHgBA...` |
| `&lt;CURRENCY&gt;` | **Required.**&lt;br&gt;&lt;br&gt;Target currency for the cloned (new) Messaging account. | `INR` |
| `&lt;EXTENDED_CREDIT_ID&gt;` | **Optional.**&lt;br&gt;&lt;br&gt;Line of Credit identifier. Required only if migrating to Line of Credit billing. If the Messaging account uses credit card billing, omit this parameter — migration works regardless of the current payment method. | `987654321098765` |

### Example request

```curl
curl &#039;https://graph.facebook.com/v23.0/123456789012345/set_payment_method_migration_intent&#039; \
-H &#039;Content-Type: application/json&#039; \
-H &#039;Authorization: Bearer EAABsbCS1iHgBA...&#039; \
-d &#039;
&#123;
  &quot;currency&quot;: &quot;INR&quot;,
  &quot;extended_credit_id&quot;: &quot;987654321098765&quot;
&#125;&#039;
```

### Example response

```json
&#123;
  &quot;migration_id&quot;: &quot;mig_01HZYK3ABCDEF4567890&quot;,
  &quot;migration_status&quot;: &quot;INITIATED&quot;
&#125;
```

## Check migration status

Use the GET /&lt;MIGRATION_ID&gt; endpoint to check the current status of a migration. Poll this endpoint to monitor progress until the status reaches `READY_TO_COMPLETE` or `COMPLETED`.

### Request syntax

```html
curl &#039;https://graph.facebook.com/&lt;API_VERSION&gt;/&lt;MIGRATION_ID&gt;&#039; \
-H &#039;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&#039;
```

### Request parameters

| Placeholder | Description | Example Value |
| --- | --- | --- |
| `&lt;MIGRATION_ID&gt;`&lt;br&gt;&lt;br&gt;_String_ | **Required.**&lt;br&gt;&lt;br&gt;The `migration_id` returned by the initiate migration endpoint. | `mig_01HZYK3ABCDEF4567890` |

### Example request

```curl
curl &#039;https://graph.facebook.com/v23.0/mig_01HZYK3ABCDEF4567890&#039; \
-H &#039;Authorization: Bearer EAABsbCS1iHgBA...&#039;
```

### Example response

```json
&#123;
  &quot;status&quot;: &quot;READY_TO_COMPLETE&quot;,
  &quot;destination_waba&quot;: &#123;
    &quot;id&quot;: &quot;998877665544332&quot;,
    &quot;name&quot;: &quot;Acme WABA (INR)&quot;,
    &quot;currency&quot;: &quot;INR&quot;,
    &quot;timezone_id&quot;: &quot;1&quot;,
    &quot;message_template_namespace&quot;: &quot;1234abcd_namespace&quot;
  &#125;,
  &quot;id&quot;: &quot;mig_01HZYK3ABCDEF4567890&quot;
&#125;
```

## Pre-completion verification

Before completing the migration, verify the following on the new (destination) Messaging account:

- **Templates**: Confirm that your templates have been cloned to the new Messaging account. Templates with outdated formats may not migrate. Note that template IDs on the new Messaging account will differ from the original Messaging account.
- **Flows**: Confirm that Flows used by your templates appear on the new Messaging account. Flows not used by any template are not migrated.
- **App installation**: Verify that your app is installed on the new Messaging account.
- **Users**: Confirm that users and permissions have been synced correctly to the new Messaging account.

Once you have verified these items, proceed to [Complete migration](#complete-migration).

## Complete migration

Once the migration status reaches `READY_TO_COMPLETE`, call the resume migration endpoint as the final step. This switches billing for your existing phone numbers from the old Messaging account to the new one. The numbers themselves do not move.

### Prerequisites

Before completing the migration:

- Verify that the migration status is `READY_TO_COMPLETE` by [checking the migration status](#check-migration-status).
- The new currency in the input is not the same as the existing currency on the Messaging account.
- If your migration requires Line of Credit billing, have your `CreditLine` identifier ready to attach.

After this step completes:

- The new Messaging account becomes the active account for your existing phone numbers.
- The old Messaging account can no longer send messages.
- Continue referencing the old Messaging account for historical insights and analytics.

**Request syntax**

```html
curl -X POST &quot;https://graph.facebook.com/&lt;API_VERSION&gt;/&lt;MIGRATION_ID&gt;/resume_migration&quot; \
-H &quot;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&quot;
```

**Response example**

```json
&#123;
  &quot;status&quot;: &quot;&lt;STATUS&gt;&quot;,
  &quot;destination_waba&quot;: &#123;
    &quot;id&quot;: &quot;&lt;CLONED_WABA_ID&gt;&quot;,
    &quot;name&quot;: &quot;&lt;CLONED_WABA_NAME&gt;&quot;,
    &quot;currency&quot;: &quot;&lt;NEW_CURRENCY&gt;&quot;,
    &quot;timezone_id&quot;: &quot;&lt;CLONED_WABA_TIMEZONE&gt;&quot;,
    &quot;message_template_namespace&quot;: &quot;&lt;NAMESPACE_FOR_TEMPLATES&gt;&quot;
  &#125;,
  &quot;id&quot;: &quot;&lt;MIGRATION_ID&gt;&quot;
&#125;
```

## Verify migration

After the migration status is `COMPLETED`, run these checks to confirm the new Messaging account is operational.

### Messaging account cloning and asset migration &#123;#waba-cloning-and-asset-migration&#125;

- In Meta Business Suite, under **Messaging Accounts**, verify you see two Messaging accounts: the original (original currency) and the new one (new currency).
- In the new Messaging account, verify that templates have been migrated.
- Confirm the new Messaging account is linked to the same WhatsApp account hierarchy, so your existing business phone numbers send under it.

### Messaging validation

- Send a test message from the new Messaging account using one of your existing business phone numbers.
- Confirm the message is delivered successfully and that message and cost insights appear under the new Messaging account.

## Insights and analytics after migration

Insights and analytics do not migrate to the new Messaging account. The original Messaging account is not deleted — it remains visible in all linked Business Managers for historical reference. After migration:

- **Historical data**: Continue querying the old Messaging account ID for all historical insights, analytics, and billing data generated before the migration.
- **New data**: All new messaging insights, analytics, and billing data will appear under the new Messaging account ID after migration is complete.

## Original Messaging account after migration &#123;#original-waba-after-migration&#125;

The original Messaging account is not deleted after migration. It remains visible in all linked Business Managers and accessible for historical reference. There is no plan to automatically delete original Messaging accounts.

- The original Messaging account can no longer send messages after the migration is complete.
- All historical insights, analytics, and billing data remain on the original Messaging account.
- The new Messaging account becomes the active account for your existing phone numbers, with the migrated assets.

## Migration status values

The following status values are returned by the migration API. For error statuses, see the recommended actions in the [Troubleshooting](#troubleshooting) section below.

| Status | Description |
| --- | --- |
| `INITIATED` | Migration has been initiated. The system is validating the source Messaging account and beginning asset cloning. |
| `ACCEPTED` | Migration request has been accepted and is queued for processing. |
| `IN_PROGRESS` | Assets such as templates and the Flows they use are being cloned to the new Messaging account. |
| `READY_TO_COMPLETE` | Asset cloning is finished. You can now call the resume migration endpoint to complete the migration. |
| `COMPLETED` | Migration is complete. The new Messaging account is now the billing account. |
| `FAILED` | Migration failed during asset cloning. |
| `FAILED_TO_COMPLETE` | Migration failed during the final completion step (billing account switch). |
| `REJECTED` | Migration request was rejected due to validation errors. |

## Troubleshooting

| Status | Issue | Possible reasons and solutions |
| --- | --- | --- |
| `REJECTED` | Migration request was rejected due to validation errors. | Verify that you have admin access to the source Messaging account and that your access token has the required permissions. Check that the source Messaging account is eligible for migration and retry. |
| `FAILED` | Migration failed during asset cloning (templates, Flows). | Initiate a new migration by calling the `set_payment_method_migration_intent` endpoint again. If the issue persists, contact support. |
| `FAILED_TO_COMPLETE` | Migration failed during the final completion step (billing account switch). | Call the resume migration endpoint again to retry. If the issue persists, contact support. |
| `IN_PROGRESS` (extended) | Migration has been in progress longer than expected. | Continue polling the [check migration status](#check-migration-status) endpoint. Migration duration varies depending on the number of templates and assets. If the status does not change after an extended period, contact support. |



---

Full documentation index for this product: https://developers.facebook.com/documentation/business-messaging/whatsapp/llms.txt
