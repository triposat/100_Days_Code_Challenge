from collections import Counter


def Dict_Intersection(Test_string_1, Test_string_2):
    Test_Dict_1 = Counter(Test_string_1)
    Test_Dict_2 = Counter(Test_string_2)
    Result = Test_Dict_1 & Test_Dict_2
    return Test_Dict_1 == Result


if __name__ == "__main__":
    Test_string_1 = 'ABHISHEKsinGH'
    Test_string_2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if Dict_Intersection(Test_string_1, Test_string_2):
        print("Possible")
    else:
        print("Not Possible")
