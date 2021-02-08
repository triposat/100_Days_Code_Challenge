def Tuple_Elements_divisble(Test_list, k):
    return [sub for sub in Test_list if all(ele % k == 0 for ele in sub)]


Test_list = [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
k = int(input("Enter Divisor: "))
print(Tuple_Elements_divisble(Test_list, k))
