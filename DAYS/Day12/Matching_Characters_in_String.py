def Matching_Characters_in_String(String1, String2):
    Result = []
    for words in String1:
        if words in String2:
            Result.append(words)
    return Result


String1 = input("Enter a String: ")
String2 = input("Enter a String: ")
print(*(Matching_Characters_in_String(String1, String2)))
