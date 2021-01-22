import re


def URL_from_string(Test_string):
    return re.findall("(https?://[^\s]+)", Test_string)


Test_string = "These are the links http://www.google.com  and http://stackoverflow.com/questions/839994/extracting-a-url-in-python"
print("\n".join(URL_from_string(Test_string)))
