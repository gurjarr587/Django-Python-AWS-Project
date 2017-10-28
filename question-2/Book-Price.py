#assigning the values 

cover_price = 25
discount = .10
shipping_cost_firstfive = 2
shipping_cost_rest = 0.0275
total_copies = 40

#returns the wholesale price after doing calculation in function cost()

def cost(total_copies):
	price_after_discount = cover_price * total_copies * (1-discount)
	price_after_shipping = price_after_discount + shipping_cost_firstfive + shipping_cost_rest
	return price_after_shipping

#print the total wholesale cost,calling function cost() to execute

print("the wholesale price is",cost(total_copies))
	















