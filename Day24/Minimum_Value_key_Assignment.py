def Minimum_Values_Key(Test_dict_1, Test_dict_2):
    return {key: min(value, Test_dict_2[key]) for key, value in Test_dict_1.items()}


Test_dict_1 = {"Code": 1, "Challenge": 7, "is": 8, "Best": 10}
Test_dict_2 = {"Code": 5, "Challenge": 5, "is": 7, "Best": 14}
print(Minimum_Values_Key(Test_dict_1, Test_dict_2))
