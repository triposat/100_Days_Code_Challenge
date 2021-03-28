# Approach 1:


def get_Odd_Occurrence(Test_list):
    a = set(Test_list)
    hey = {i: Test_list.count(i) for i in a}
    return [key for key, values in hey.items() if values % 2 != 0]


Test_list = [4, 5, 4, 5, 2, 2, 3, 3, 2, 4, 4]

print(*get_Odd_Occurrence(Test_list))


# Approach 2:


def get_Odd_Occurrence(Test_list):
    Result = 0
    for ele in Test_list:
        Result ^= ele
    return Result


Test_list = [4, 5, 4, 5, 2, 2, 3, 3, 2, 4, 4]
print(get_Odd_Occurrence(Test_list))
