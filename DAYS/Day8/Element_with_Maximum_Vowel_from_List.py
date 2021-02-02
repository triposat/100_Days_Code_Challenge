def Maximum_Vowel(Test_list):
    Max_String = 0
    Result = ""
    for ele in Test_list:
        count = 0
        for element in ele:
            if element in "aeiouAEIOU":
                count += 1
        if count > Max_String:
            Max_String = count
            Result = ele
    return Result


Test_list = ["gfg", "beaeioust", "for", "geeks"]
print(Maximum_Vowel(Test_list))