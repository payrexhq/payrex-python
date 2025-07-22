# Changelog

## [1.7.2] - 2025-07-22

- Support cancel payment intent.

## [1.7.1] - 2025-07-11

- Support setup_future_usage on Billing Statement.

## [1.7.0] - 2025-06-24

- Return billing_statement_merchant_name and billing_statement_number in Billing Statement resource.

## [1.6.1] - 2025-06-02

- Return net_amount in Payout Transaction resource.

## [1.6.0] - 2025-05-30

- Add update payment endpoint.

## [1.5.0] - 2025-05-30

- Add list payout transactions endpoint.
- Add Payout and PayoutTransaction resources.

## [1.4.0] - 2025-05-15

- Add get payment by id endpoint

## [1.3.0] - 2025-04-23

- Add customer session endpoints.

## [1.2.1] - 2025-04-23

- Add update support for refunds.

## [1.2.0] - 2025-02-10

- Add billing_details_collection support for checkout sessions.
- Add billing_details_collection support for billing statements.

## [1.1.0] - 2025-02-07

- Add statement_descriptor support for payment intents.
- Add statement_descriptor support for billing statements.

## [1.0.2] - 2024-12-04

- Resolve bug.

## [1.0.1] - 2024-10-02

- Add send billing statement via email endpoint.

## [1.0.0] - 2024-09-04

- Add billing statement endpoints
- Add customer endpoints

Breaking change
- Standardize the use of arrays in resources. The `payment_intent` attribute of CheckoutSession resource is now an array. Previously, this attribute is a PaymentIntent resource.

## [0.1.5] - 2024-07-30

- Add amount_capturable and amount_received for hold then capture partial amount support.

## [0.1.4] - 2024-07-25

- Adjust building of parameter query due to changes in checkout session endpoints.

## [0.1.3] - 2024-07-23

- Remove deprecated capture_type attribute. capture_type should now be referenced via payment_method_options.card.capture_type.

## [0.1.2] - 2024-07-21

- Add payment_method_options in PaymenIntent resource.

## [0.1.1] - 2024-05-24

- Update error handling.

## [0.1.0] - 2024-05-16

- Initial alpha release.
