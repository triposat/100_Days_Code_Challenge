from collections import defaultdict


def Join_Tuples(Test_list):
    Result = defaultdict(list)
    for key, value in Test_list:
        Result[key].append(value)
    return [(key, *value) for key, value in Result.items()]


Test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
print(Join_Tuples(Test_list))
