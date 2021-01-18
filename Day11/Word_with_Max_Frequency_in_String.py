def Words_Frequency(Test_String):
    hey = {keys: Test_String.count(keys) for keys in Test_String.split()}
    return max(hey, key=hey.get)


Test_String = input("Enter a String: ")
print(Words_Frequency(Test_String))
