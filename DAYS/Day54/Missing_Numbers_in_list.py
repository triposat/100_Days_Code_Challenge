def missing_numbers(Test_list):
    Result = [x for x in range(Test_list[0], Test_list[-1] + 1)]
    return (list(set(Test_list) ^ set(Result)))


print(missing_numbers([1, 2, 3, 4, 6, 7, 10]))
print(missing_numbers([10, 11, 12, 14, 17]))
