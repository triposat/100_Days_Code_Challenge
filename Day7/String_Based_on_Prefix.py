def String_Prefix(Test_list, Prefix_list):
    return [ele for ele in Test_list if any(ele.startswith(element) for element in Prefix_list)]


Test_list = ["geeks", "peeks", "meeks", "leeks", "mean"]
Prefix_list = ["ge", "ne", "me", "re"]
print(String_Prefix(Test_list, Prefix_list))
