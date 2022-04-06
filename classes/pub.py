class Pub:
    def __init__(self, input_name, input_drinks):
        self.name = input_name
        self.drinks = input_drinks
        self.till = 100

    def sell_drink(self, drink):
        self.till += drink.price

    