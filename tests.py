import unittest
from checkout import SupermarketCheckout

class TestSupermarketCheckout(unittest.TestCase):
    def setUp(self):
        """
        Set up a new SupermarketCheckout instance before each test case.
        """
        self.checkout = SupermarketCheckout()

    def test_empty_cart(self):
        """
        Test that the total is 0 when the cart is empty.
        """
        self.assertEqual(self.checkout.calculate_total(), 0)
        
    def test_single_item(self):
        """
        Test the total price for a single item.
        """
        self.checkout.scan("A")
        self.assertEqual(self.checkout.calculate_total(), 50)

    def test_multiple_items(self):
        """
        Test the total price for multiple items in various combinations.
        """
        test_cases = [
            ("AB", 80),
            ("CDBA", 115),
            ("AA", 100),
            ("AAA", 130),
            ("AAAA", 180),
            ("AAAAA", 230),
            ("AAAAAA", 260),
            ("AAAB", 160),
            ("AAABB", 175),
            ("AAABBD", 190),
            ("DABABA", 190),
            ("AABBCC", 185),  # Test multiple items without special offers
            ("ABCDD", 130),   # Test multiple items with some having special offers
            ("ABCAABD", 210)  # Test multiple items with different combinations of special offers
        ]

        for test_input, expected_output in test_cases:
            with self.subTest(test_input=test_input):
                for item in test_input:
                    self.checkout.scan(item)
                total = self.checkout.calculate_total()
                self.assertEqual(total, expected_output, f"Test failed for input: {test_input}")
                self.checkout.cart.clear()

    def test_items_not_in_price_list(self):
        """
        Test scanning items that are not in the price list.
        """
        with self.assertRaises(ValueError) as context:
            self.checkout.scan("E")

        self.assertIn("Item 'E' not found in the price list.", str(context.exception))

if __name__ == "__main__":
    unittest.main()
