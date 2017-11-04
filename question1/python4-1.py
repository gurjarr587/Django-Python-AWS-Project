#this function returns output in the form of list using concept of recursive function

def permutations(string):

    output = set([string])
    if len(string) == 2:
        output.add(string[1] + string[0]) # here switching the first letter of string with second

    elif len(string) > 2:
             for i in range(len(string)):
                for perm in permutations(string[:i] + string[i + 1:]):#iterating through the permutations
                    output.add(string[i] + perm)#adding the above two reversed string with the first letter
    return list(output)

def permutations2(string2):

    output = set([string2])
    if len(string2) == 2:
        output.add(string2[1].upper() + string2[0].upper())  # here switching the first letter of string with second

    if len(string2) == 2:
        output.add(string2[1] + string2[0])  # here switching the first letter of string with second

    if len(string2) == 2:
        output.add(string2[1] + string2[0].upper())  # here switching the first letter of string with second

    if len(string2) == 2:
        output.add(string2[1].upper() + string2[0])  # here switching the first letter of string with second


    return list(output)


print(permutations('a'))#returns permutation of a after calling function permutation

print(permutations('ab'))#returns permutation of ab after calling function permutation

print(permutations('aabb'))#returns permutation of aabb after calling function permutation

print(permutations('hello'))#returns permutation of hello after calling function permutation

print(permutations2('ab'))#returns permutation of hello after calling function permutation
