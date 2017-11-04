#This function returns the total counts of a number to perform persistence and  decleared global variables count and prod

global count

def persistence(number):#updating the count value over here
    count = 0
    prod = 1
    ind_num = list(str(number))
    a = len(ind_num)

    if  a > 9:
        for i in range(len(ind_num)):
            prod *= int(ind_num[i])
        if num > 9:
            count += 1
            persistence(prod)#function calling functon for calculation number greater than 1
        else:
            count += 1


    else:#if number is not greater than 1 then it returns value of count

        return count

print(persistence(25))#returns the number of counts needed to do persistence
print(persistence(4))#returns the number of counts needed to do persistence
print(persistence(999))#returns the number of counts needed to do persistence



#Initialising counter to 0
cntr = 0
def persistence(numm):
    global cntr
    # split integer into a number
    num = str(numm)
    num_list = list(num)   # prepares a list with converted string
    new_num = 1
    if numm > 9:
        for i in range(len(num_list)):
            new_num *= int(num_list[i])
        if new_num > 9:
            cntr = cntr + 1
            persistence(new_num)
## calling the recursion function until the number is greater than 9
        else:
            cntr = cntr + 1
    else:
        cntr = 0
## else dont increment counter
    return cntr
numb = int(input("Enter the number: "))
print("Counter ", persistence(numb))