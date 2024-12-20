# Changelog

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
