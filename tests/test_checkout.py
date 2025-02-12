import pytest
from src.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_calculate_total(checkout):
    checkout.add_item_with_price("capuccino", 5)
    checkout.add_item("capuccino")
    assert checkout.calculate_total() == 5


def test_calculate_total_of_multiple_items(checkout):
    checkout.add_item_with_price("capuccino", 5)
    checkout.add_item_with_price("espresso", 3)
    checkout.add_item("capuccino")
    checkout.add_item("espresso")
    assert checkout.calculate_total() == 8