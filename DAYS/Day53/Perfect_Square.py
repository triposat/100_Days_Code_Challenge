import math


def perfect_square(num):
    if num > 0:
        root = math.sqrt(num)
        return root*root == num
    return False


num = int(input("Enter a Number: "))
print(perfect_square(num))
