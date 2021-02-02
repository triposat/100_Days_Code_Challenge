from collections import OrderedDict


def Order_of_Character(Test_string, Pattern):
    Test_dict = OrderedDict.fromkeys(Test_string)
    count = 0
    for key, _ in Test_dict.items():
        if key == Pattern[count]:
            count += 1
        if count == len(Pattern):
            return 'True'
    return 'False'


Test_string = input("Enter String: ")
Pattern = input("Enter Pattern: ")
print(Order_of_Character(Test_string, Pattern))