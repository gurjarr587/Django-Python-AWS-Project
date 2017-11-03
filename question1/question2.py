
# 1. From the provided input text file “File_to_be_read.txt” please perform the following mentioned tasks.

#A. Read the data from the input file using a try and catch block and using with keyword, scan through the entire file and count the number of occurrences of each word and write the data into a new file with name as “output1.txt”.

try:
    f = open("File_to_be_read_relatedto_Assignment_3.1.txt","r")
except IOError:
    print("error")
else:
    with f:

        str1 = f.read().replace("\n","")
        str2 = str1.lower()
        str2 = str2.split()

        count1 = str1.count(' he ')
        count2 = str2.count("pointed")
        count3 = str2.count('his')
        count4 = str2.count("finger")
        count5 = str2.count("in")
        count6 = str2.count("friendly")
        count7 = str2.count("jest")
        count8 = str2.count('and')
        count9 = str2.count("went")
        count10 = str2.count("over")
        count11 = str2.count("to")
        count12 = str2.count("the")

        print("\n","He:", count1, "\n", "pointed:", count2, "\n","his:", count3, "\n","finger:", count4, "\n","in:", count5, "\n","friendly:", count6, "\n","jest:", count7, "\n","and:", count8, "\n","went:", count9, "\n","over:", count10, "\n","to:", count11, "\n","the:", count12, "\n")
        output1 = open("output1.txt", "w")
        print("\n","He:", count1, "\n", "pointed:", count2, "\n", "his:", count3, "\n", "finger:", count4, "\n", "in:",
              count5, "\n", "friendly:", count6, "\n", "jest:", count7, "\n", "and:", count8, "\n", "went:", count9,
              "\n", "over:", count10, "\n", "to:", count11, "\n", "the:", count12, "\n", file=output1)

        f.close()
#B. Read the data from the input file using a try and catch block and using with keyword, scan through  ch line of the file and count the length of each word and write the data into a new text file “output2.txt”.

try:
    f1 = open("File_to_be_read_relatedto_Assignment_3.1.txt","r")
except IOError:
    print("error")
else:
    with f1:
        strb1 = f1.read().replace("\n","")
        strb2 = strb1.lower()
        strb2 = strb2.split()
        key = ["He","pointed","his","finger","in","friendly","jest","and","went","over","to"]
        for i in key:
            for j in strb2:
                if len(i) == len(j):
                    break
            output2 = open("output2.txt", "a")
            print(i, len(i), sep=",")
            print(i, len(i), sep=",",file=output2)
            f1.close()

