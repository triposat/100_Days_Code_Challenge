def Merge_Dictionaries(Test_dict_1, Test_dict_2):
    return Test_dict_1.update(Test_dict_2)


Test_dict_1 = {'A': 10, 'B': 8}
Test_dict_2 = {'D': 6, 'C': 4}
Merge_Dictionaries(Test_dict_1, Test_dict_2)
print(Test_dict_1)