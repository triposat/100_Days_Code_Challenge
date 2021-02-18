import re


def Remove_all(Test_string):
    return re.sub(r"[\W_]+", "", Test_string)


Test_string = "123abcjw:, .@! eiw"
print(Remove_all(Test_string))
