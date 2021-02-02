def Remove_Duplicates(Test_list):
    Result = []
    for element in Test_list:
        if element not in Result:
            Result.append(element)
    return Result


Test_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
print(Remove_Duplicates(Test_list))
