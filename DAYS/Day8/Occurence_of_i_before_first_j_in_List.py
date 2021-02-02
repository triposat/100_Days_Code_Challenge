# Approach 1:

def Occurence(Test_list, i, j):
    count = 0
    for ele in Test_list:
        if ele == j:
            break
        if ele == i:
            count += 1
    return count


Test_list = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9]
i, j = 4, 8
print(Occurence(Test_list, i, j))

# Approach 2:

def Occurence(Test_list, i, j):
    Index = Test_list.index(j)
    Temp = Test_list[:Index]
    return Temp.count(i)


Test_list = [4, 5, 6, 4, 1, 4, 8, 5, 4, 3, 4, 9]
i, j = 4, 8
print(Occurence(Test_list, i, j))
