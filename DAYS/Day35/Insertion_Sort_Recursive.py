def Insertion_Sorting_Recur(Test_list, n):
    if n <= 1:
        return
    Insertion_Sorting_Recur(Test_list, n-1)
    last = Test_list[n-1]
    j = n-2
    while(j >= 0 and last < Test_list[j]):
        Test_list[j+1] = Test_list[j]
        j -= 1
    Test_list[j+1] = last


Test_list = [14, 18, 11, 56, 12, 32, 5]
Insertion_Sorting_Recur(Test_list, len(Test_list))
print(Test_list)
