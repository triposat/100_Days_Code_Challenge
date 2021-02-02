def Swap_ith_with_jth(Test_list, i, j):
    for ele in range(len(Test_list)):
        if Test_list[ele] is i:
            Test_list[ele] = j
        elif Test_list[ele] is j:
            Test_list[ele] = i
    return Test_list


Test_list = [4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]
i, j = 4, 8
print(Swap_ith_with_jth(Test_list, i, j))