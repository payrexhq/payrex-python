# PayRex Python

PayRex Python library provides Python applications an easy access to the PayRex API. Explore various Python classes that represents PayRex API resources on object instantiation.

## Requirements

Python 3.9.+

## Installation

If you want to use the package, run the following command:

```sh
pip install payrex-python
```

If you want to build the library from source:

Create a virtual environment

```sh
python -m venv venv
```

Activate the virtual environment

```sh
source venv/bin/activate
```

Install the package to the virtual environment

```sh
pip install -e /Your/Local/Path/payrex-python

python
```

## Getting Started

Simple usage looks like:

```python
from payrex import Client as PayrexClient

payrex_client = PayrexClient('sk_test_...')
payment_intent = payrex_client.payment_intents.retrieve('pi_...')

payment_intent = payrex_client.payment_intents.create(
    {
        'amount': 10000,
        'currency': 'PHP',
        'description': 'Dino Treat',
        'payment_methods': ['gcash']
    }
)
```

## Handle errors

```python
try:
    payrex_client = PayrexClient('sk_test_...')

    payment_intent = payrex_client.payment_intents.create(
        {
            'amount': 10000,
            'description': 'Dino Treat',
            'payment_methods': ['gcash']
        }
    )
except BaseException as e:
    # Handle error
    print(type(e))
    print(e.errors[0].code)
    print(e.errors[0].detail)
    print(e.errors[0].parameter)
```

## Verify webhook signature

```python
try:
    payload = '{"id":"evt_...","resource":"event","type":"payment_intent.succeeded","data":{...'
    signature_header = 't=1715236958,te=,li=...'
    webhook_secret_key = 'whsk_...'

    payrex_client.webhooks.parse_event(
        payload,
        signature_header,
        webhook_secret_key
    )
except SignatureVerificationException as e:
    # Handle invalid signature
```
