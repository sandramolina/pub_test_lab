import unittest
from classes.customer import *

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Mad Max", 1000)

    def test_customer_name(self):
        self.assertEqual("Mad Max", self.customer1.name)

    def test_customer_wallet(self):
        self.assertEqual(1000, self.customer1.wallet)
