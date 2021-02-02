from collections import Counter


def Possible_Words(Test_list, Test_chars):
    for words in Test_list:
        count = 1
        Char = dict(Counter(words))
        for key in words:
            if key not in Test_chars:
                count = 0
            else:
                if Test_chars.count(key) != Char[key]:
                    count = 0
        if count == 1:
            print(words)


if __name__ == "__main__":
    Test_list = ['go', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
    Test_chars = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    Possible_Words(Test_list, Test_chars)
