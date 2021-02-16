import re

def Put_Spaces(Test_string):
    words = re.findall('[A-Z][a-z]*', Test_string)
    Result = [word.lower() for word in words]
    print(" ".join(Result))


if __name__ == "__main__":
    Test_string = 'BruceWayneIsBatman'
    Put_Spaces(Test_string)
