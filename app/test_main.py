import pytest
from datetime import date
from freezegun import freeze_time
from app.main import outdated_products


@pytest.fixture(scope="module")
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2022, 2, 1),
            "price": 160
        }
    ]


@freeze_time("2022-02-05")
def test_today_not_outdated(
    products: list
) -> None:
    result = outdated_products(products)
    assert "duck" in result
    assert "chicken" in result
    assert "salmon" in result
