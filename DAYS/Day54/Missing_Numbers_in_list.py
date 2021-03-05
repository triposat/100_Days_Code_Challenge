def missing_number(Test_list):
    return sum(range(Test_list[0], Test_list[-1]+1)) - sum(Test_list)


Test_list_1 = [1, 2, 3, 5, 6, 7, 8]
Test_list_2 = [10, 11, 12, 14, 15, 16, 17]
print(missing_number(Test_list_1))
print(missing_number(Test_list_2))
