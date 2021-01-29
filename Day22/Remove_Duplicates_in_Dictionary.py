def Remove_Duplicates(Test_string):
    Test_list = []
    for elements in Test_string.split(" "):
        if ((Test_string.count(elements) > 1 or Test_string.count(elements) == 1) and elements not in Test_list):
            Test_list.append(elements)
    return Test_list


Test_string = input("Enter a String: ")
print(*(Remove_Duplicates(Test_string)))