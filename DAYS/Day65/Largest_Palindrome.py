def Largest_Prime(num):
    Upper_limit = (10**(num))-1
    Lower_limit = 1+Upper_limit//10
    Low_range = Upper_limit-Lower_limit
    Max_product = 0
    for i in range(Upper_limit, Low_range, -1):
        for j in range(i, Low_range, -1):
            number = str(i*j)
            if number == number[::-1]:
                Max_product = i*j
                return Max_product


if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    print(Largest_Prime(num))
