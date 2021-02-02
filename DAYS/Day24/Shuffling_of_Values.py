# Approach 1:

import random


def Shuffling_of_Value(Test_dict):
    Temp_dict = list(Test_dict.values())
    random.shuffle(Temp_dict)
    return dict(zip(Test_dict, Temp_dict))


Test_dict = {"Code": 1, "Challenge": 7, "is": 8, "Best": 10}
print(Shuffling_of_Value(Test_dict))


from random import sample

# Approach 2:

def Shuffling_of_Value(Test_dict):
    return dict(zip(Test_dict, sample(list(Test_dict.values()), len(Test_dict))))


Test_dict = {"Code": 1, "Challenge": 7, "is": 8, "Best": 10}
print(Shuffling_of_Value(Test_dict))
