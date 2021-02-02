from collections import OrderedDict


def Non_Repeating_Character(Test_string, K_Value):
    Test_dict = OrderedDict.fromkeys(Test_string, 0)
    for characters in Test_string:
        Test_dict[characters] += 1
    Non_Repeating_Char = [key for key, value in Test_dict.items() if value == 1]
    if len(Non_Repeating_Char) < K_Value:
        return "Alert! Wrong"
    else:
        return Non_Repeating_Char[K_Value-1]


Test_string = input("Enter a String: ")
K_Value = int(input("K: "))
print(Non_Repeating_Character(Test_string, K_Value))
