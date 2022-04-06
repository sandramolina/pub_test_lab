import unittest
from classes.customer import *
from classes.drink import  *

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Mad Max", 1000, 29)
        self.first_drink = Drink("Rum and Coke", "cocktail", 8)

    def test_customer_name(self):
        self.assertEqual("Mad Max", self.customer1.name)

    def test_customer_wallet(self):
        self.assertEqual(1000, self.customer1.wallet)

    def test_customer_age(self):
        self.assertEqual(29, self.customer1.age)

    def test_buy_drink_function(self):
        self.customer1.buy_drink(self.first_drink)
        self.assertEqual(992, self.customer1.wallet)
