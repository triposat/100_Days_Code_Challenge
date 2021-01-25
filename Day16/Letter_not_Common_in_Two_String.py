def Letters_not_common(Test_String_1, Test_String_2):
    return list(set(Test_String_1) ^ set(Test_String_2))


Test_String_1 = input("Enter 1st String: ")
Test_String_2 = input("Enter 2nd String: ")
print(*(Letters_not_common(Test_String_1, Test_String_2)))
