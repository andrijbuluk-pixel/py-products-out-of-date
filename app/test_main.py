import pytest
from datetime import date


from app.main import outdated_products


@pytest.fixture(scope="module")
def products() -> list:
    return [
        {"name": "salmon",
         "expiration_date": date(2022, 2, 10),
         "price": 600
         },
        {"name": "chicken",
         "expiration_date": date(2022, 2, 5),
         "price": 120
         },
        {"name": "duck",
         "expiration_date": date(2022, 2, 1),
         "price": 160
         },
    ]

