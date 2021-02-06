def Nested_Tuple(Test_tuple, Test_keys):
    return [{key: value for key, value in zip(Test_keys, tuples)} for tuples in Test_tuple]


Test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
Test_keys = ['key', 'value', 'id']
print(Nested_Tuple(Test_tuple, Test_keys))
