class product:
    def __init__(self, name, price, discountpercent):
        self.name = name
        self.price = price
        self.discountpercent = discountpercent

    def getDiscountAmount(self):
        return self.price * self.discountpercent / 100

    def getDiscountPrice(self):
        return self.price-self.getDiscountAmount()



