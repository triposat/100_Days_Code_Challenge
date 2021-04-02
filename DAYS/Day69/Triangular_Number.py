def divisor(num):
    Result = []
    for i in range(1, int(num)):
        if num % i == 0:
            Result.append(i)
    return Result


def triangular_number(num):
    count = True
    natural = 1
    while count:
        ctr = (natural*(natural+1))/2
        if len(divisor(ctr)) >= num:
            return int(ctr)
        natural += 1


if __name__ == "__main__":
    num = int(input("Enter n: "))
    print(triangular_number(num))
