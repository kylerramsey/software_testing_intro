from hashlib import new
from tkinter import N
from shopping_cart import Cart, CartItem
import unittest

class TestShoppingcart(unittest.TestCase):
    def test_clear_items(self):
        cart = Cart()
        new_item = CartItem('mango', 1.99)
        cart.add_item(new_item)

        # test the data that was passed into the CartItem class
        cart.clear_cart()
        self.assertEqual(len(cart.items), 0)

    def test_populate_items(self):
        cart = Cart()
        new_item = CartItem('mango', 1.99)
        cart.add_item(new_item)
        self.assertEqual(new_item.name, 'mango')
        self.assertEqual(new_item.price, 1.99)

    def test_check_if_item_exists(self):
        cart = Cart()
        new_item = CartItem('mango', 1.99)
        cart.add_item(new_item)

        new_item.price = 2.99
        self.assertIn(new_item, cart.items)



if __name__ == '__main__':
    unittest.main()