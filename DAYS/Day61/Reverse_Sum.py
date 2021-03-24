def Reverse_Sum(num1, num2):
    return int(str(int(str(num1)[::-1]) + int(str(num2)[::-1]))[::-1])


if __name__ == "__main__":
    print(Reverse_Sum(13, 14))
    print(Reverse_Sum(130, 1))
    print(Reverse_Sum(305, 794))


