def power(Num1):
    while Num1 % 2 == 0:
        Num1 /= 2
    return Num1 == 1


Num1 = int(input("Enter a Number: "))
print(power(Num1))
