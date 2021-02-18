import re


def Vowel_String(Test_string):
    pattern = "^[aeiouAEIOU][a-zA-Z0-9]*"
    if re.search(pattern, Test_string):
        print("Accepted")
    else:
        print("Discarded")


Test_string1 = "code"
Test_string2 = "expression20"
Vowel_String(Test_string1)
Vowel_String(Test_string2)
