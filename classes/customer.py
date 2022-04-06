class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age

    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price
