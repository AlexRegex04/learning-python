class Shopping:
    def __init__(self):
        self.ballance = 1000
        self.price = {"jeans":200, "shirt":300}
        self.cart = []
       #buy item:
        self.opi = input("yes or no ")
        
    def add_to_cart (self, item):
        self.cart.append(item)
        self.item = item
    def buy(self):
        if self.opi == "yes":
            self.ballance = self.ballance - self.price[self.item]
            print("Your current ballance: ",str(self.ballance))
        elif self.opi == 'no':
            print("Your current ballance: ",str(self.ballance))
# now test this
my_shop = Shopping()
my_shop.add_to_cart('jeans')
print( my_shop.cart)
my_shop.buy()
