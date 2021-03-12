def single_digit(Num):
    Result = map(int, str(Num))
    Total = sum(list(Result))
    if Total < 10:
        print(Total)
    else:
        single_digit(Total)


Num = int(input("Enter a Number: "))
single_digit(Num)
