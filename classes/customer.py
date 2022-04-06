class Customer:
    def __init__(self, input_name, input_wallet, input_age):
        self.name = input_name
        self.wallet = input_wallet
        self.age = input_age
        self.drunkness = 0.0

    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price
        self.drunkness_level(drink_to_buy)
    
    def drunkness_level(self, drink):
        self.drunkness += drink.alcohol_level

    def buy_food(self, food):
        self.wallet -= food.food_price
        self.drunkness -= food.rejuvenation_level