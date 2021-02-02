def Symmetric(Test_String):
    length = len(Test_String)//2
    if len(Test_String) % 2 == 0 and str(Test_String[0:length]) == str(Test_String[length:]):
        return "Symmetric"
    else:
        return "Unsymmetric"


def Palindrome(Test_String):
    if Test_String == Test_String[::-1]:
        return "Palindrome"
    else:
        return "Not Plaindrome"


Test_String = input("Enter a String: ")
print(Symmetric(Test_String))
print(Palindrome(Test_String))
