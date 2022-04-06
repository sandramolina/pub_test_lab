class Customer:
    def __init__(self, input_name, input_wallet):
        self.name = input_name
        self.wallet = input_wallet

    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price
