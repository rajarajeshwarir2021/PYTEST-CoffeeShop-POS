# CoffeePOS - Coffee Shop Point of Sale System

## Overview
CoffeePOS is a simple Point of Sale (POS) system for a coffee shop, designed as a test project using `pytest`. It calculates the total price of customer orders, applies discounts, and ensures correct pricing rules are followed.

## Features
- Customers can order different coffee and snack items.
- Each item has a fixed price.
- Discounts are applied based on special pricing rules:
  - **Buy 2 Cappuccinos, Get 1 Free**
  - **Buy a Croissant with any coffee and get 10% off on the Croissant**
- Computes the total price after applying discounts.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/CoffeePOS.git
   cd CoffeePOS
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running Tests
The project uses `pytest` for testing. To run the tests, use:
```sh
pytest
```

## Project Structure
```
pytest_coffeepos/
│── src/
│   ├── checkout.py      # Checkout system logic
│   ├── pricing_rules.py # Pricing and discount rules
│   └── __init__.py
│── tests/
│   ├── test_checkout.py # Unit tests for checkout
│   ├── test_discounts.py # Tests for discount rules
│   └── __init__.py
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
```

## Example Usage
```python
from src.checkout import Checkout

checkout = Checkout()
checkout.add_item("Cappuccino")
checkout.add_item("Cappuccino")
checkout.add_item("Croissant")

total = checkout.calculate_total()
print(f"Total: ${total:.2f}")
```

## Contributing
Feel free to submit pull requests or report issues if you’d like to improve this project!

## License
This project is licensed under the MIT License.

