import re


def String_start_with_Substring(Test_string, Test_sample):
    Result = "^"+Test_sample
    if re.search(Result, Test_string):
        return "True"
    else:
        return "False"


Test_string = "100 Days of Code Challenge makes your basic clear"
Test_sample = "100"
print(String_start_with_Substring(Test_string, Test_sample))
