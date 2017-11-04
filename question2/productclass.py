from object import product

product1 = product("stanley 13 ounce wood hammer",12.99,62)
product2 = product("National Hardware 3/4 wire nails",5.06,0)

print("Name:        {:s}".format(product1.name))
print("Price:        {:.3f}".format(product1.price))
print("Discount Percent: {:d}%".format(product1.discountpercent))
print("Discount Amount: {:.2f}".format(product1.getDiscountAmount()))
print("Dsicount Price: {:.1f}".format(product1.getDiscountPrice()))