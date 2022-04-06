import unittest
from classes.drink import Drink
from classes.pub import Pub
from classes.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.customer1 = Customer("Mad Max", 1000, 29)
        self.customer2 = Customer("Joan of Arc", 50, 15)
        self.drink_list1 = Drink("Mojito", "Cocktail", 12, 0.10)
        self.pub_1 = Pub("SanDraagon", self.drink_list1)

    def test_pub_name(self):
        self.assertEqual("SanDraagon", self.pub_1.name)

    def test_pub_till(self):
        self.assertEqual(100, self.pub_1.till)

    def test_pub_drinks(self):
        self.assertEqual(self.drink_list1, self.pub_1.drinks)

    def test_sell_drink_function(self):
        self.pub_1.sell_drink(self.drink_list1, self.customer1)
        self.assertEqual(112, self.pub_1.till)

    def test_sell_drink_function_no_sell(self):
        self.assertEqual("Please come back lateeeer", self.pub_1.sell_drink(self.drink_list1, self.customer2))

    def test_sell_drink_when_drunked_customer(self):
        self.customer1.drunkness = 0.5        
        self.assertEqual("Please go to sleep", self.pub_1.sell_drink(self.drink_list1, self.customer1))

    def test_drink_stock_levels(self):
        mojito_stock = self.pub_1.drinks_stock[1]["stock_levels"]
        self.assertEqual(40, mojito_stock)

    def test_total_stock(self):
        total_stock_value = self.pub_1.stock_value_calculator(self.pub_1.drinks_stock)
        self.assertEqual(630, total_stock_value)