from collections import defaultdict

class SupermarketCheckout:
    """
    A class representing a supermarket checkout system.

    Attributes:
        prices (dict): A dictionary mapping item codes to their respective prices.
        special_offers (dict): A dictionary mapping item codes to special offer details.
        cart (defaultdict): A defaultdict representing the items scanned by the customer and their quantities.
    """

    def __init__(self):
        """
        Initializes a new instance of the SupermarketCheckout class.

        The checkout system is initialized with default prices, special offers, and an empty cart.
        """
        self.prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
        self.special_offers = {'A': (3, 130), 'B': (2, 45)}
        self.cart = defaultdict(int)

    def scan(self, item):
        """
        Adds an item to the cart or increments its quantity if it already exists.

        Args:
            item (str): The code representing the item to be scanned.
        Raises:
            ValueError: If the item code is not found in the price list.
        """
        if item in self.prices:
            self.cart[item] += 1
        else:
            raise ValueError(f"Item '{item}' not found in the price list.")

    def calculate_total(self):
        """
        Calculates the total price of the items in the cart, considering special offers.

        Returns:
            int: The total price of the items in the cart.
        """
        total_price = 0
        for item, quantity in self.cart.items():
            total_price += self.calculate_item_price(item, quantity)
        return total_price

    def calculate_item_price(self, item, quantity):
        """
        Calculates the price of a specific item based on its quantity and any applicable special offers.

        Args:
            item (str): The code representing the item.
            quantity (int): The quantity of the item.

        Returns:
            int: The price of the item based on its quantity and special offers.
        """
        if item in self.special_offers:
            special_quantity, special_price = self.special_offers[item]
            special_offer_count = quantity // special_quantity
            remaining_count = quantity % special_quantity
            return special_offer_count * special_price + remaining_count * self.prices[item]
        else:
            return quantity * self.prices[item]
