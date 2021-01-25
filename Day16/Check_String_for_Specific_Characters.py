def Check_String_for_Specific_Characters(Test_string, Test_list):
    Result = []
    for char in Test_list:
        if char in Test_string:
            Result.append('True')
        else:
            Result.append('False')

    return Result


Test_string = "@geeksfor#geeks123%^&*"
Test_list = ['#', '%', '8', '@', ')']
print(Check_String_for_Specific_Characters(Test_string, Test_list))


def Check_String_for_Specific_Characters(Test_string, Test_list):
    return [char in Test_string for char in Test_list]


Test_string = "@geeksfor#geeks123%^&*"
Test_list = ['#', '%', '8', '@', ')']
print(Check_String_for_Specific_Characters(Test_string, Test_list))
