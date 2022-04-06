import unittest

from classes.pub import Pub

class TestPub(unittest.TestCase):
    
    def setUp(self):
        
        self.pub_1 = Pub("SanDraagon", ["Ale"])

    def test_pub_name(self):
        self.assertEqual("SanDraagon", self.pub_1.name)

    def test_pub_till(self):
        self.assertEqual(100, self.pub_1.till)

    def test_pub_drinks(self):
        self.assertEqual("Ale". self.pub_1.drinks)