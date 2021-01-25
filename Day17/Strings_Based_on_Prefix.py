def Prefix_Strings(Test_list, Pref_list):
    return [ele for ele in Test_list if any(ele.startswith(el) for el in Pref_list)]


Test_list = ["geeks", "peeks", "meeks", "leeks", "mean"]
Pref_list = ["ge", "ne", "me", "re"]
print(*(Prefix_Strings(Test_list, Pref_list)))
