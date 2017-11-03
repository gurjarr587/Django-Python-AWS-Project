#this is function which returns with the value of Matrix in 2-D form with the required pattern desired by peter the postman 10*10 matrix and 5*5 matrix

def mailbox():
    c = "c"
    O = "O"
    o = "o"
    w = int(input("enter no of rows:"))
    h = int(input("enter no of columns:"))
    Matrix = [[c for i in range(w)] for j in range(h)]


    if w%2 == 0 or w%3:# checking condition for even values of rows
        for i in range(w):
            for j in range(h):

                if i != 0 and j % 2 != 0 and i == 1:  # checking condition for position by using in j modulous 2
                    Matrix[i][j] = O
                    Matrix[i + 1][j] = Matrix[i][j]

                if i%2 == 0 and j%2 == 0 and i != 0:
                    Matrix[i][j] = Matrix[i][j]
                    if Matrix[i][j] == "O":
                        Matrix[i][j] = o

                if i%3 == 0 and j%3 == 0 and j != 0 and i != 0:
                    Matrix[i][j] = O

        return Matrix

    else:

        for i in range(w):#checking condition if neither the row or column odd or even
            for j in range(h):

                if i != 0 and j % 2 != 0 and i == 1:  # checking condition for position by using in j modulous 2
                    Matrix[i][j] = O
                    Matrix[i + 1][j] = Matrix[i][j]

                if i%2 == 0 and j%2 == 0 and i != 0:
                    Matrix[i][j] = Matrix[i][j]
                    if Matrix[i][j] == "O":
                        Matrix[i][j] = o

                if i%3 == 0 and j%3 == 0 and j != 0 and i != 0:
                    Matrix[i][j] = O
        return Matrix


# priting the returned matirx from above function
print(mailbox())




