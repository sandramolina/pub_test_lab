class Pub:
    def __init__(self, input_name, input_drinks):
        self.name = input_name
        self.drinks = input_drinks
        self.till = 100

    def sell_drink(self, drink, customer):
        if customer.age >= 18:
            if customer.drunkness < 0.50:
                self.till += drink.price
            else:
                return "Please go to sleep"

        else:
            return "Please come back lateeeer"
    