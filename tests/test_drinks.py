import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink_list1 = Drink("Beavertown", "Beer", 5, 0.02)
    
    def test_drink_name(self):
        self.assertEqual("Beavertown", self.drink_list1.brand_name)

    def test_drink_type(self):
        self.assertEqual("Beer", self.drink_list1.type)

    def test_drink_price(self):
        self.assertEqual(5, self.drink_list1.price) 

    def test_drink_alcohol_level(self):
        self.assertEqual(0.02, self.drink_list1.alcohol_level) 