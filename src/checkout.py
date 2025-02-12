class Checkout:
    def __init__(self):
        self.product_price = {}
        self.total_price = 0

    def add_item_with_price(self, item, price):
        self.product_price[item] = price

    def add_item(self, item):
        self.total_price += self.product_price[item]

    def add_discount_rule(self, item, quantity, discount):
        return

    def calculate_total(self):
        return self.total_price
