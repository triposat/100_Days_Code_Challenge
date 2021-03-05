def power(num1, num2):
    while(num1 % num2 == 0):
        num1 /= num2
    return num1 == 1


num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
print(power(num1, num2))
