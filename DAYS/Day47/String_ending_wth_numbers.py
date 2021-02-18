import re


def string_ending(Test_string):
    pattern = "[a-zA-Z0-9]$"
    if re.search(pattern, Test_string):
        print("Accepted")
    else:
        print("Discarded")


Test_string1 = "satyam@"
Test_string2 = "satyamempire5623"
Test_string3 = "satyam."
Test_string4 = "heysatyamhere"
string_ending(Test_string1)
string_ending(Test_string2)
string_ending(Test_string3)
string_ending(Test_string4)
