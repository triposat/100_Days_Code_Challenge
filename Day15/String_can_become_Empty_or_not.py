def Empty_or_not(Test_string, Sub_String):
    if len(Test_string) == 0 and len(Sub_String) == 0:
        return 'True'
    if len(Sub_String) == 0:
        return "True"
    while(len(Test_string) != 0):
        index = Test_string.find(Sub_String)
        if index == -1:
            return "False"
        else:
            Test_string = Test_string[0:index] + \
                Test_string[index+len(Sub_String):]
    return "True"


Test_string = input("Enter a String: ")
Sub_String = input("Enter a Sub-String: ")
print(Empty_or_not(Test_string, Sub_String))
