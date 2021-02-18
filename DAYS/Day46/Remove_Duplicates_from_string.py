import re


def Remove_Duplicates(Test_string):
    Pattern = r"\b(\w+)(?:\W\1\b)+"
    return re.sub(Pattern, r"\1", Test_string, flags=re.IGNORECASE)


Test_string1 = "Good bye bye world world"
Test_string2 = "Ram went went to to his home"
Test_string3 = "Hello hello world world"
print(Remove_Duplicates(Test_string1))
print(Remove_Duplicates(Test_string2))
print(Remove_Duplicates(Test_string3))
