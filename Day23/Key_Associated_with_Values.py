from collections import defaultdict


def Key_Associated(Test_dict):
    Result = defaultdict(list)
    for key, value in Test_dict.items():
        for ele in value:
            Result[ele].append(key)

    return dict(Result)


Test_dict = {'Code': [1, 2, 3], "Challenge": [
    3, 4, 5], 'is': [1, 4], 'best': [4, 2]}
print(Key_Associated(Test_dict))
