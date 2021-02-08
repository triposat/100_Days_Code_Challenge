def Sort_Tuple(Test_list):
    Test_list.sort(key=lambda Sub: max(Sub), reverse=True)
    return Test_list


Test_list = [(4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
print(Sort_Tuple(Test_list))
