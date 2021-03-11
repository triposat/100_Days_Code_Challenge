def Occur_twice(Test_list):
    Result = 0
    for i in Test_list:
        Result ^= i
    return Result


Test_list = [5, 3, 4, 3, 4]
print(Occur_twice(Test_list))
