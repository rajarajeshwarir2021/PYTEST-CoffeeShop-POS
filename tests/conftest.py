import pytest

from src.checkout import Checkout


@pytest.fixture()
def checkout():
    """Fixture to initialize a Checkout instance with sample products."""
    checkout = Checkout()
    checkout.add_item_with_price("cappuccino", 5)
    checkout.add_item_with_price("espresso", 3)
    return checkout
