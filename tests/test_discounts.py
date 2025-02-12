from pytest import approx


def test_add_multiple_discount_rule(checkout):
    """Test applying multiple discount rules to different items."""
    # Adding discount rules (20% off on 2 Cappuccinos, 10% off on 2 Espressos)
    checkout.add_discount_rule("cappuccino", 2, 20)
    checkout.add_discount_rule("espresso", 2, 10)

    # Adding items to the checkout
    checkout.add_item("cappuccino")
    checkout.add_item("cappuccino")
    checkout.add_item("espresso")
    checkout.add_item("espresso")

    # Expected total:
    # 2 Cappuccinos (5 * 2 * 0.8 = 8.0)
    # 2 Espressos (3 * 2 * 0.9 = 5.4)
    # Total = 8.0 + 5.4 = 13.4

    assert checkout.calculate_total() == approx(13.4)
