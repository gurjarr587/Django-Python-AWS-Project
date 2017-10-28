#return's the value after calculating in the formula for celsius. 
def fahrenheit(celsius):
  return ((celsius*(9/5)+32))

#user inputs a value and then condition is checked that it is in celcius or not then printing the return value with separation of space.

celsius_temp_inpt = input("set the temperature in celsius:")
celsius_temp = float(celsius_temp_inpt[0:-1])
if celsius_temp_inpt[-1] == 'C':
   celsius = celsius_temp
print("the temperature in fahrenheit is:",fahrenheit(celsius),'F',sep=' ') #calling function fahrenheit to execute 
 
