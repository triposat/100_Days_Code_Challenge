def Maximum_Uppercase(Test_string):
    count = 0
    Result = 0
    Store_1 = ''
    Store_2 = ''
    for indexes in range(0, len(Test_String)):
        if Test_String[indexes].isupper():
            Store_1 += Test_String[indexes]
            count += 1
        else:
            Result = count
            Store_2 = Store_1
            Store_1 = ''
            count = 0
    if Test_String[len(Test_String)-1].isupper():
        Result = count
        Store_2 = Store_1

    return Store_2, Result


Test_String = input("Enter a String: ")
print(*(Maximum_Uppercase(Test_String)))
