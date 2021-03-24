def move_zero_end(Test_list):
    Zero = [0 for i in Test_list if i == 0]
    Result = [i for i in Test_list if i != 0]
    Result.extend(Zero)
    return Result


print(move_zero_end([0, 2, 3, 4, 6, 7, 10]))
print(move_zero_end([10, 0, 11, 12, 0, 14, 17]))
