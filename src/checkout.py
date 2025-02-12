class Checkout:
    """
    Checkout system for a coffee shop that supports item pricing,
    adding items, applying discounts, and calculating the total cost.
    """

    class Discount:
        """
        Represents a discount rule for an item.
        Attributes:
            quantity (int): The minimum quantity required to apply the discount.
            discount (float): The discount percentage applied when the rule is met.
        """

        def __init__(self, quantity: int, discount: float):
            self.quantity = quantity
            self.discount = discount

    def __init__(self):
        """
        Initializes the Checkout system with:
        - `product_price`: A dictionary storing item prices.
        - `items`: A dictionary tracking item quantities in the cart.
        - `discounts`: A dictionary storing discount rules for items.
        """
        self.product_price = {}  # Stores item prices
        self.items = {}  # Stores items added to the checkout
        self.discounts = {}  # Stores discount rules

    def add_item_with_price(self, item: str, price: float):
        """
        Adds an item and its price to the product list.
        Args:
            item (str): Name of the item.
            price (float): Price of the item.
        """
        self.product_price[item] = price

    def add_item(self, item: str):
        """
        Adds an item to the cart. If the item already exists, its quantity is incremented.
        Raises an exception if the item does not exist in the product list.
        Args:
            item (str): Name of the item.
        """
        if item not in self.product_price:
            raise Exception("Product does not exist")  # Prevents adding unknown products

        self.items[item] = self.items.get(item, 0) + 1  # Increment quantity

    def add_discount_rule(self, item: str, quantity: int, discount: float):
        """
        Adds a discount rule for a specific item.
        Args:
            item (str): Name of the item.
            quantity (int): Minimum quantity required for the discount.
            discount (float): Percentage discount applied.
        """
        self.discounts[item] = self.Discount(quantity, discount)

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the cart, applying discounts where applicable.
        Returns:
            float: Total price after applying discounts.
        """
        total_price = 0
        for item, quantity in self.items.items():
            total_price += self.calculate_item_total(item, quantity)
        return total_price

    def calculate_item_total(self, item: str, quantity: int) -> float:
        """
        Calculates the total price for a specific item, considering discount rules.
        Args:
            item (str): Name of the item.
            quantity (int): Quantity of the item.
        Returns:
            float: Total price for the item after applying discounts (if applicable).
        """
        if item in self.discounts and quantity >= self.discounts[item].quantity:
            discount_item = self.discounts[item]
            return (
                    self.calculate_discounted_total(discount_item, item, quantity) +
                    self.calculate_full_price_total(discount_item, item, quantity)
            )
        return self.product_price[item] * quantity  # Regular price if no discount applies

    def calculate_full_price_total(self, discount_item: Discount, item: str, quantity: int) -> float:
        """
        Calculates the total price for items that are not part of a discount set.
        Args:
            discount_item (Discount): The discount rule for the item.
            item (str): Name of the item.
            quantity (int): Quantity of the item.
        Returns:
            float: Total price for items sold at full price.
        """
        full_price_quantity = quantity % discount_item.quantity  # Items not covered by the discount
        return full_price_quantity * self.product_price[item]

    def calculate_discounted_total(self, discount_item: Discount, item: str, quantity: int) -> float:
        """
        Calculates the total price for items that qualify for a discount.
        Args:
            discount_item (Discount): The discount rule for the item.
            item (str): Name of the item.
            quantity (int): Quantity of the item.
        Returns:
            float: Total price for discounted items.
        """
        discount_sets = quantity // discount_item.quantity  # Number of sets eligible for discount
        discount_multiplier = (1 - discount_item.discount / 100)  # Convert discount % to a multiplier
        return discount_sets * discount_item.quantity * self.product_price[item] * discount_multiplier
