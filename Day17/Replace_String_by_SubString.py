def Replace_Words(Test_string, Sub_1, Sub_2):
    return Test_String.replace(Sub_1, Sub_2)


Test_String = input("Enter a String: ")
Sub_1 = input("Which: ")
Sub_2 = input("To: ")
print(Replace_Words(Test_String, Sub_1, Sub_2))
