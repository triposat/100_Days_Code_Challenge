# Approach 1:

def Remove_Row_with_Custom_Element(Test_list, Check_list):
    for row in Test_list:
        for ele in Check_list:
            if ele in row:
                Test_list.remove(row)
    return Test_list


Test_list = [[5, 3, 1], [7, 8, 9], [1, 10, 22], [12, 18, 21]]
Check_list = [3, 10, 19, 29, 20, 15]
print(Remove_Row_with_Custom_Element(Test_list, Check_list))




# Approach 2:

def Remove_Row_with_Custom_Element(Test_list, Check_list):
    return [row for row in Test_list if not any(ele in row for ele in Check_list)]


Test_list = [[5, 3, 1], [7, 8, 9], [1, 10, 22], [12, 18, 21]]
Check_list = [3, 10, 19, 29, 20, 15]
print(Remove_Row_with_Custom_Element(Test_list, Check_list))
