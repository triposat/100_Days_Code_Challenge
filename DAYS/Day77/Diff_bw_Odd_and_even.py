
# Approach 1:

def Difference(num):
    Even = 0
    Odd = 0
    Result = str(num)
    for i in range(len(Result)):
        if i % 2 == 0:
            Even += int(Result[i])
        else:
            Odd += int(Result[i])
    return Odd-Even == 0


if __name__ == "__main__":
    num = int(input("Enter Number: "))
    if Difference(num):
        print("Yes")
    else:
        print("No")


# Approach 2:

def Difference(num):
    return (num % 11 == 0)


if __name__ == "__main__":
    num = int(input("Enter Number: "))
    if Difference(num):
        print("Yes")
    else:
        print("No")
