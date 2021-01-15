# Approach 1:

def Element_Multiple(Test_list, Check_list):
    Result = []
    for ele in Test_list:
        count = 0
        for element in Check_list:
            if ele % element == 0:
                count += 1
        if count == len(Check_list):
            Result.append(ele)
    return Result


Test_list = [4, 24, 8, 10, 12, 23]
Check_list = [6, 4]
print(Element_Multiple(Test_list, Check_list))

# Approach 2:

def Element_Multiple(Test_list, Check_list):
    return [ele for ele in Test_list if all(ele % element == 0 for element in Check_list)]


Test_list = [4, 24, 8, 10, 12, 23]
Check_list = [6, 4]
print(Element_Multiple(Test_list, Check_list))
