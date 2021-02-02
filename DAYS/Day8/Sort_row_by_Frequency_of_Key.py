# Approach 1:

def length(row):
    return row.count(n)


def Sort_Row(Test_list, n):
    Test_list.sort(key=length)
    return Test_list

Test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]
n = 2
print(Sort_Row(Test_list, n))


# Approach 2:

def Sort_Row(Test_list, n):
    Result = sorted(Test_list, key=lambda row: row.count(n))
    return Result


Test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]
n = 2
print(Sort_Row(Test_list, n))
