from src.drinks_stock import *

class Pub:
    def __init__(self, input_name, input_drinks):
        self.name = input_name
        self.drinks = input_drinks
        self.till = 100
        self.drinks_stock = drinks_stock

    def sell_drink(self, drink, customer):
        if customer.age >= 18:
            if customer.drunkness < 0.50:
                self.till += drink.price
            else:
                return "Please go to sleep"

        else:
            return "Please come back lateeeer"
    
    def stock_value_calculator(self, stock_list):
        stock_value = 0
        for i in range(len(stock_list)):
            stock_value_drink = stock_list[i]["price"] * stock_list[i]["stock_levels"]
            stock_value += stock_value_drink
        return stock_value