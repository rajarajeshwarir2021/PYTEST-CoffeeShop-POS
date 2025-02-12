class Checkout:

    class Discount:
        def __init__(self, quantity, discount):
            self.quantity = quantity
            self.discount = discount

    def __init__(self):
        self.product_price = {}
        self.items = {}
        self.discounts = {}

    def add_item_with_price(self, item, price):
        self.product_price[item] = price

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def add_discount_rule(self, item, quantity, discount):
        discount = self.Discount(quantity, discount)
        self.discounts[item] = discount

    def calculate_total(self):
        total_price = 0
        for item, quantity in self.items.items():
            item_total = self.calculate_item_total(item, quantity)
            total_price += item_total
        return total_price

    def calculate_item_total(self, item, quantity):
        item_total = 0
        if item in self.discounts:
            discount_item = self.discounts[item]
            if quantity >= discount_item.quantity:
                item_total += self.calculate_discounted_total(discount_item, item, quantity)

                item_total += self.calculate_full_price_total(discount_item, item, quantity)
            else:
                item_total += self.product_price[item] * quantity
        else:
            item_total += self.product_price[item] * quantity

        return item_total

    def calculate_full_price_total(self, discount_item, item, quantity):
        full_price_quantity = quantity % discount_item.quantity
        full_price = full_price_quantity * self.product_price[item]
        return full_price

    def calculate_discounted_total(self, discount_item, item, quantity):
        discount_quantity = quantity / discount_item.quantity
        discount = (1 - (discount_item.discount / 100))
        discount_price = discount_quantity * quantity * self.product_price[item] * discount
        return discount_price
