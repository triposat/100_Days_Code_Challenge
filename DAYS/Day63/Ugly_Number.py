def Ugly_number(num):
    for ele in [2, 3, 5]:
        while num % ele == 0:
            num /= ele
    return num == 1


if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    print(Ugly_number(num))
