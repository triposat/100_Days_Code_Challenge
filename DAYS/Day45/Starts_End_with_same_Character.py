import re


def Starts_End(Pattern, Test_string):
    if re.search(Pattern, Test_string):
        print("Valid...")
    else:
        print("Invalid...")


if __name__ == "__main__":
    Pattern = r'^[a-z]$|^([a-z]).*\1$'
    Test_string = "abba"
    Starts_End(Pattern, Test_string)
