from collections import Counter


def Check_Binary_Representation(Num_1, Num_2):
    Bin_1 = bin(Num_1)[2:]
    Bin_2 = bin(Num_2)[2:]
    Zeroes = abs(len(Bin_1)-len(Bin_2))
    if len(Bin_2) > len(Bin_1):
        Bin_1 = Zeroes*'0'+Bin_1
    else:
        Bin_2 = Zeroes*'0'+Bin_2
    Dict_1 = Counter(Bin_1)
    Dict_2 = Counter(Bin_2)
    if Dict_1 == Dict_2:
        return "True"
    else:
        return "False"


Num_1 = int(input("1st Number: "))
Num_2 = int(input("2nd Number: "))
print(Check_Binary_Representation(Num_1, Num_2))
