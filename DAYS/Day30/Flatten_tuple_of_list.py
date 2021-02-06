def Flatten_Tuple(Test_tuple):
    return tuple(sum(Test_tuple, []))


Test_tuple = ([5, 6], [6, 7, 8, 9], [3])
print(Flatten_Tuple(Test_tuple))
