def Insertion_Sorting(Test_list):
    for i in range(len(Test_list)):
        key = Test_list[i]
        j = i-1
        while(j >= 0 and key < Test_list[j]):
            Test_list[j+1] = Test_list[j]
            j -= 1
        Test_list[j+1] = key
    return Test_list


Test_list = [14, 18, 11, 56, 12, 32, 5]
print(Insertion_Sorting(Test_list))