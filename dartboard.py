#arbitrary argument this function returns the total score as count for different values
def scoreThrows(*r):
	
	
	count = 0
	for i in r:				# i inside the argument values *r 
		if(i>10):
			count += 0
			
		elif(i>=5 and i<=10):
			count += 5
			
		elif(i<5):
			count += 10
		else:
			count
	return count		
				
# to execute function and print the output

x = scoreThrows() 
print (x)	

# to execute function and print the output

x = scoreThrows(1,5,11) 
print (x)

# to execute function and print the output

y = scoreThrows(15,20,30) 
print (y)

# to execute function and print the output with bonus of 100

z = scoreThrows(1,2,3,4)+100 
print(z)

# to execute function and print the output

w = scoreThrows(1,2,3,4,5,6,7,8,9) 
print(w)



