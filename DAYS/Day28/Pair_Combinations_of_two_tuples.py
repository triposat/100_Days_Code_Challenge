def Pair_Combinations(Test_tuple_1, Test_tuple_2):
    return [(a, b) for a in Test_tuple_1 for b in Test_tuple_2] +\
        [(a, b) for a in Test_tuple_2 for b in Test_tuple_1]


Test_tuple_1 = (4, 5)
Test_tuple_2 = (7, 8)
print(Pair_Combinations(Test_tuple_1, Test_tuple_2))
