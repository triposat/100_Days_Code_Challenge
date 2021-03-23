def Reverse_bits(Num, Bit_size):
    binary = bin(Num)
    reverse = binary[:1:-1]
    Result = reverse+(Bit_size-len(reverse))*"0"
    return int(Result, 2)


if __name__ == "__main__":
    Num = int(input("Enter a Number: "))
    Bit_size = int(input("Enter Bit Size: "))
    print(Reverse_bits(Num, Bit_size))
