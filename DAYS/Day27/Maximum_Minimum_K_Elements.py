def Max_Min_Elements(Test_tup, K):
    Test_tup = list(Test_tup)
    Temp_Tup = sorted(Test_tup)
    return tuple(Temp_Tup[:K]+Temp_Tup[-K:])


Test_tup = (5, 20, 3, 7, 6, 8, 2, 87, 9, 14)
K = int(input("K: "))
print(Max_Min_Elements(Test_tup, K))