import math


def Largest_Prime_Factor(num):
    count = 2
    Prime_Factor = 1
    while count <= math.sqrt(num):
        if not num % count == 0:
            Prime_Factor = count
            count += 1
        else:
            num /= count

    if Prime_Factor < num:
        Prime_Factor = num
    return int(Prime_Factor)


if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    print(Largest_Prime_Factor(num))
