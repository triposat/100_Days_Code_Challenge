def Maximum_Index(Test_dict):
    return {key: Test_dict[key].index(max(Test_dict[key])) for key in Test_dict}


Test_dict = {"Challenges": [5, 3, 6, 3], "are": [1, 7, 5, 3], "Best": [9, 1, 3, 5]}
print(Maximum_Index(Test_dict))
