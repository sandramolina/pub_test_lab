import unittest
from classes.customer import *
from classes.drink import  *

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Mad Max", 1000, 29)
        self.first_drink = Drink("Rum and Coke", "cocktail", 8, 0.10)

    def test_customer_name(self):
        self.assertEqual("Mad Max", self.customer1.name)

    def test_customer_wallet(self):
        self.assertEqual(1000, self.customer1.wallet)

    def test_customer_age(self):
        self.assertEqual(29, self.customer1.age)

    def test_customer_drunkness(self):
        self.assertEqual(0.0, self.customer1.drunkness)

    def test_buy_drink_function(self):
        self.customer1.buy_drink(self.first_drink)
        self.assertEqual(992, self.customer1.wallet)
    
    def test_drunkness_level(self):
        self.customer1.drunkness_level(self.first_drink)
        self.assertEqual(0.10, self.customer1.drunkness)
