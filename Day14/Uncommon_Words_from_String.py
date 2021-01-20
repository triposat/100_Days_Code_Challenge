def Uncommon_Words(String1, String2):
    Result = ""
    for words in String1.split():
        if words not in String2.split():
            Result += words+" "
    for words in String2.split():
        if words not in String1.split():
            Result += words+" "
    return Result


String1 = input("Enter 1st String: ")
String2 = input("Enter 2nd String: ")
print(Uncommon_Words(String1, String2))