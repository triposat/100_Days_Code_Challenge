# Approach 1:

from collections import defaultdict


def Index_Directory(Test_list):
    Result = defaultdict(list)
    for key in set(Test_list):
        for index, value in enumerate(Test_list):
            if key == value:
                Result[key].append(index)
    return dict(Result)


Test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
print(Index_Directory(Test_list))

# Approach 2:

def Index_Directory(Test_list):
    return {key: [index for index, value in enumerate(Test_list) if value == key] for key in set(Test_list)}


Test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
print(Index_Directory(Test_list))
