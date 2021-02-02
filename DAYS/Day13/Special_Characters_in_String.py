import string
def Special_Characters_String(Test_string):
    Special_Characters = string.punctuation
    if any(elements in Special_Characters for elements in Test_string):
        return "Not Accepted"
    else:
        return "Accepted"


Test_string = input("Enter a String: ")
print(Special_Characters_String(Test_string))