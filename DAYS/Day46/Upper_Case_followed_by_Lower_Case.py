import re


def Match_Chars(Test_string):
    Pattern = "[A-Z]+[a-z]+$"
    if re.search(Pattern, Test_string):
        print("Yes")
    else:
        print("No")


Test_string1 = "CodeChallenge"
Test_string2 = "codechallenge"
Test_string3 = "codeChallenge"
Match_Chars(Test_string1)
Match_Chars(Test_string2)
Match_Chars(Test_string3)
