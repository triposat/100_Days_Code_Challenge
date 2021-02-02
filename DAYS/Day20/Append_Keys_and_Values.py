def Append_Keys_and_Values(Test_list):
    return list(Test_list.keys())+list(Test_list.values())


Test_list = {"Code": 1, "Challenge": 10, "is": 100, "Best": 1000}
print(Append_Keys_and_Values(Test_list))