#function to returns the hidden word which is missing

def hidden(num):

    key =""
    key = {'6': "a", '1': "b", '7': "d", '4': "e", '3': "i", '2': "l", '9': "m", '8': "n", '0': "o", '5': "t"}#given key values in question

    word=""

    for i in str(num):

        word+=key[i]

    return word
#calling function to execute for the numbers and find the missing word and print it
print(hidden(637))
print(hidden(7468))
print(hidden(49632))
print(hidden(1425))
print(hidden(6250))
print(hidden(12674))
print(hidden(4735))
print(hidden(7345))
print(hidden(3850))
print(hidden(2394))
print(hidden(2068))
print(hidden(137))
print(hidden(1065))
print(hidden(6509))
print(hidden(3549))
print(hidden(5394))
print(hidden(56124))
print(hidden(968))
print(hidden(103247))
print(hidden(67935))
print(hidden(7415))
print(hidden(2687))
print(hidden(261))
print(hidden(8054))
print(hidden(942547))
