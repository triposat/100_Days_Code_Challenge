def Duplicate_Charaters(Test_String):
    Duplicates = []
    for char in Test_String:
        if Test_String.count(char) > 1 and char not in Duplicates:
            Duplicates.append(char)
    return Duplicates


Test_String = input("Enter a String: ")
print(*(Duplicate_Charaters(Test_String)))
