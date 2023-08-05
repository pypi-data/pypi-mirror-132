# vatcompliance api python library

## Library install

The official documentation is located [here](https://developers.vatcompliance.co/omp-tax-rate-api/)

## Getting Started
```
pip install vatcompliance
```

## Package Dependencies
* [Requests](https://github.com/kennethreitz/requests) HTTP library for making RESTful requests to the Vatcompliance API.

Example Request
```
import vatcompliance

client = vatcompliance.Client(api_key='5bedbd829e7442f3a18589ca99fc15b0')
result = client.omp_feed(
    {
        "transaction_id": "ttt4565-85546",
        "transaction_datetime": "2020-01-09T08:27:22 +00:00",
        "transaction_sum": 158.04,
        "currency": "GBP",
        "arrival_country" : "GBR",
        "arrival_city" : "London",
        "arrival_address_line" : "Peckham Road",
        "transaction_status" : "Success",
        "good_code": "62160000",
        "merchant_establishment_country_id": "GBR",
        "vat_percent": 20.00,
        "vat": 28.73,
        "departure_country" : "AUS",
        "getParams": {
            "if_digital": True,
            "if_vat_calculate": True,
        }
    }
)
```

if you se in method POST ?if_digital={true/false}&if_vat_calculate={true/false} set the given parameter in the array as:
```
	"getParams": {
            "if_digital": True,
            "if_vat_calculate": True,
        }
```
