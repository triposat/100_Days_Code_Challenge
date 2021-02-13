def Inverted_Star(n):
    for i in range(n, 0, -1):
        print((n-i)*' ' + i * '*')


n = int(input("Enter N: "))
Inverted_Star(n)
