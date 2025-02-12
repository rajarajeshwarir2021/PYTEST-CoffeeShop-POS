from src.checkout import Checkout


def test_add_item_with_price():
    co = Checkout()
    co.add_item_with_price("capuccino", 5)