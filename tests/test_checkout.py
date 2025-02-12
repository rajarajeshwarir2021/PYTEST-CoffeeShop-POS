import pytest
from src.checkout import Checkout


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_calculate_total(checkout):
    checkout.add_item_with_price("capuccino", 5)
    checkout.add_item("capuccino")
    assert checkout.calculate_total() == 1
