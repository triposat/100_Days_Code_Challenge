import re


def Check_Defined_Characters(Test_String, pattern):
    if re.search(pattern, Test_String):
        print("Valid String...")
    else:
        print("Invalid String...")


pattern = re.compile("^[1234]+$")
Check_Defined_Characters('2134', pattern)
Check_Defined_Characters('349', pattern)
