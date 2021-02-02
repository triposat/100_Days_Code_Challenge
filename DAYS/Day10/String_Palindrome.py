def Palindrome(Test_String):
    if Test_String == Test_String[::-1]:
        return True
    else:
        return False


Test_String = input("Enter a String: ")
print(Palindrome(Test_String))
