def Sort_Tuple(Test_list):
    return sorted(Test_list, key= lambda Test_Tuple: sum(len(str(ele)) for ele in Test_Tuple))

Test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
print(Sort_Tuple(Test_list))