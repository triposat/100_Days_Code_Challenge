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


def Hamming_sequence(num):
    if num == 1:
        return 1
    Hamming_sequence(num-1)
    if is_Hamming(num) == True:
        print(num, end=" ")


if __name__ == "__main__":
    print("Hamming Sequence: ")
    Hamming_sequence(24)
