def Extract_digit(Test_list):
    Result = ""
    for key, value in Test_list:
        Result += str(key)+str(value)
    return [int(ele) for ele in set(Result)]


Test_list = [(15, 3), (3, 9), (1, 10), (99, 2)]
print(Extract_digit(Test_list))
