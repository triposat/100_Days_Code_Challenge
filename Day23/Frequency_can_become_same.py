from collections import Counter


def Check_Frequency(Test_string):
    Test_dict = Counter(Test_string)
    Result = list(set(Test_dict.values()))
    if len(Result) > 2:
        return False
    elif len(Result) == 2 and Result[1]-Result[0] > 1:
        return False
    else:
        return True


Test_string = "xxxyyzz"
if Check_Frequency(Test_string):
    print("Yes")
else:
    print("No")
