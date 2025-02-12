import pytest
from src.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_add_item_with_price(checkout):
    checkout.add_item_with_price("capuccino", 5)


def test_add_item(checkout):
    checkout.add_item("capuccino")
