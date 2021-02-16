import re


def Extract_Maximum(Test_string):
    # Result=re.findall(r"[0-9]+", Test_string)
    Result=re.findall("\d+", Test_string)
    return max(Result)

Test_string = '100klh564abc365bg'
print(Extract_Maximum(Test_string))