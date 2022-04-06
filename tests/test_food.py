import unittest

from classes.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food1 = Food("Fish and Chips", 8, 0.20)
    
    def test_food_name(self):
        self.assertEqual("Fish and Chips", self.food1.food_name)
    
    def test_food_price(self):
        self.assertEqual(8, self.food1.food_price)