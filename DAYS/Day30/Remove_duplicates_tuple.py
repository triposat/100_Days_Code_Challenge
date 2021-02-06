def Remove_Duplicates(Test_list):
    Result = [tuple(sorted(tuples)) for tuples in Test_list]
    return list(set(Result))


Test_list = [(4, 6), (1, 2), (9, 2), (2, 1), (5, 7), (6, 4), (9, 2)]
print(Remove_Duplicates(Test_list))
