def Maximum_Key(Test_list):
    Result = {}
    for dictionary in Test_list:
        for key, value in dictionary.items():
            if key in Result:
                Result[key] = max(Result[key], value)
            else:
                Result[key] = value
    return Result


Test_list = [{"Days": 8, "Code": 1, "Challenge": 9},
             {"Days": 2, "Code": 9, "Challenge": 1},
             {"Days": 5, "Code": 10, "Challenge": 7}]
print(Maximum_Key(Test_list))
