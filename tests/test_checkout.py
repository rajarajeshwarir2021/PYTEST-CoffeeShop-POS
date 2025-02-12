import pytest


def test_calculate_total(checkout):
    """Test calculating total price for a single item."""
    checkout.add_item("cappuccino")
    assert checkout.calculate_total() == 5


def test_calculate_total_of_multiple_items(checkout):
    """Test calculating total price for multiple different items."""
    checkout.add_item("cappuccino")
    checkout.add_item("espresso")
    assert checkout.calculate_total() == 8  # 5 + 3


def test_throw_exception_with_bad_item(checkout):
    """Test that adding a non-existent item raises an exception."""
    with pytest.raises(Exception, match="Product does not exist"):
        checkout.add_item("dirty chai")
