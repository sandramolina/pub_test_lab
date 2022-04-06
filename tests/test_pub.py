import unittest
from classes.drink import Drink

from classes.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_list = Drink("Mojito", "Cocktail", 12)
        self.pub_1 = Pub("SanDraagon", self.drink_list)

    def test_pub_name(self):
        self.assertEqual("SanDraagon", self.pub_1.name)

    def test_pub_till(self):
        self.assertEqual(100, self.pub_1.till)

    def test_pub_drinks(self):
        self.assertEqual(self.drink_list, self.pub_1.drinks)