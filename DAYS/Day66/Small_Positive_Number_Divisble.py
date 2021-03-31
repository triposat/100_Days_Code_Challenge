import math


def small_positive(num):
    Result = 1
    for i in range(1, num+1):
        Result = int((Result*i)/math.gcd(Result, i))
    return Result


# Driver Function
if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    print(small_positive(num))
