from collections import Counter


def Max_Anagram(Test_string):
    for i in range(0, len(Test_string.split(" "))):
        Test_string[i] = ''.join(sorted(Test_string[i]))
    Dict_Frequency = Counter(Test_string)
    return max(Dict_Frequency.values())


if __name__ == "__main__":
    Test_string = 'ant magenta magnate tan gnamate'
    print(Max_Anagram(Test_string))
