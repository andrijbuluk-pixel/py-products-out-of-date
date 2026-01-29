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


@freeze_time(datetime.date(2022, 1, 2))
def test_no_outdated_products(
    products: list
) -> None:
    assert outdated_products(products) == []


@freeze_time(datetime.date(2022, 2, 2))
def test_one_outdated_product(
        products: list
) -> None:
    assert outdated_products(products) == ["duck"]


@freeze_time(datetime.date(2022, 2, 6))
def test_two_outdated_products(
    products: list
) -> None:
    assert outdated_products(products) == ["chicken", "duck"]


@freeze_time(datetime.date(2022, 2, 15))
def test_full_outdated_products(
    products: list
) -> None:
    assert outdated_products(products) == ["salmon", "chicken", "duck"]
