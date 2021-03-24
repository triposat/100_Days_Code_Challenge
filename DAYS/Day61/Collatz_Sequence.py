def Collatz_Sequence(num):
    Result = [num]
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = 3*num+1
        Result.append(num)
    return Result


if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    print(Collatz_Sequence(num))