def Inverted_Star(Test_input):
    for i in range(Test_input+1, 0, -1):
        for j in range(0, i-1):
            print("*", end=" ")
        print(" ")


Test_input = int(input("Enter N: "))
Inverted_Star(Test_input)
