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


@freeze_time("2022-01-02")
def test_no_outdated_products(
    products: list
) -> None:
    assert outdated_products(products) == []


@freeze_time("2022-02-02")
def test_one_outdated_product(
        products: list
) -> None:
    assert outdated_products(products) == ["duck"]


@freeze_time("2022-02-06")
def test_two_outdated_products(
    products: list
) -> None:
    assert outdated_products(products) == ["chicken", "duck"]


@freeze_time("2022-02-15")
def test_full_outdated_products(
    products: list
) -> None:
    assert outdated_products(products) == ["salmon", "chicken", "duck"]


@freeze_time("2022-02-05")
def test_today_not_outdated(
    products: list
) -> None:
    result = outdated_products(products)
    assert "duck" in result
    assert "chicken" in result
    assert "salmon" in result
