import re


def Most_Occur(Test_string):
    Result = re.findall(r"[0-9]+", Test_string)
    return max(Result, key=Result.count)


Test_string = 'geek55of55gee4ksabc3dr2x'
print(Most_Occur(Test_string))
