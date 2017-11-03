
def list(movie_list):
    if len(movie_list) == 0:
        print("the list of movies.\n")
        return
    else:
        i=1
        for row in movie_list:
            print(str(i) + "the name of movie"+row[0]+"( " + str(row[1]) + ")")
            i+=1
        print()

def display_menu():
    print("command , menu")
    print("list - list all the moives")
    print("add - Add movie name")
    print("del - delete the movie")
    print("exit - exit program")
    print()

def add(movie_list):
    name = input("Name:")
    year = input("year:")
    movie = []
    movie.append(name)
    movie.append(year)
    movie_list.append(movie)
    print(movie[0]+"that movie was added")

def delete(movie_list):
    number = int(input("insert the movie number"))
    if number < 1 or number > len(movie_list):
        print("this movie number is invalid")
    else:
        movie = movie_list.pop(number-1)
        print(movie[0]+"deleted.\n")

def main():
    movie_list = [["holiday", 2015],
                  ["baby",2015],
                  ["entertainment",2016]]

    display_menu()

    while True:
        command = input("command: ")
        if command == "list":
            list(movie_list)
        if command == "add":
            add(movie_list)		
        if command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("invalid input follow the above commands")
    print("!bye")

if __name__ == "__main__":
    main()

