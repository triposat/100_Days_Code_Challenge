def is_Hamming(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        return is_Hamming(num/2)
    if num % 3 == 0:
        return is_Hamming(num/3)
    if num % 5 == 0:
        return is_Hamming(num/5)
    return 0


if __name__ == "__main__":
    num = int(input("Enter a Number: "))
    if is_Hamming(num) == 1:
        print("It's a Hamming Number")
    else:
        print("It's not a Hamming Number")
