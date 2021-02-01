def Remove_Duplicity(Test_dict):
    Result = {}
    for key, value in Test_dict.items():
        Flag = True
        for Sub_key, Sub_Value in Result.items():
            if key in Sub_Value:
                Flag = False
        if Flag == True:
            Result[key] = value
    return Result


Test_dict = {'All': ['All', 'Time', 'Favourite'],
             'Favourite': ['All'], 'Code': ['Challenge']}
print(Remove_Duplicity(Test_dict))
