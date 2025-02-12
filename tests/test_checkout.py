import pytest
from pytest import approx
from src.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.add_item_with_price("capuccino", 5)
    checkout.add_item_with_price("espresso", 3)
    return checkout


def test_calculate_total(checkout):
    checkout.add_item("capuccino")
    assert checkout.calculate_total() == 5


def test_calculate_total_of_multiple_items(checkout):
    checkout.add_item("capuccino")
    checkout.add_item("espresso")
    assert checkout.calculate_total() == 8


def test_add_discount_rule(checkout):
    checkout.add_discount_rule("capuccino", 2, 20)
    checkout.add_item("capuccino")
    checkout.add_item("capuccino")
    assert checkout.calculate_total() == 8

