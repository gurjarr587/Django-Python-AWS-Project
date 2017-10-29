
#this function returns is_triangle function value after inserting user values x,y,z and then calculates and return with true or false 

def start_triangle_check():

	
	x = int(input("the value of side a is :"))
	y = int(input("the value of side b is :"))
	z = int(input("the value of side c is :"))

	return is_triangle(x,y,z)

#this function calculates the triangle can be formed or not by using already assingned values 	

def is_triangle(a,b,c):
	
	
	a = int(a)
	b = int(b)
	c = int(c)	

	if (c > a + b) or (a > c + b) or (b > a + c): #condition to check that sides can make triangle or not
       
		return False 
	else:
		
		return True 

	
#calling function start_triangle_check to execute with user values 

print(start_triangle_check())

#calling function is_triangle to execute with already assingned values 

print(is_triangle(1,12,1))

	
	


		

