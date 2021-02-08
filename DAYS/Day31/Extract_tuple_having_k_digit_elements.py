def Extract_tuple(Test_list, K):
    return [sub for sub in Test_list if all(len(str(ele)) == K for ele in sub)]


Test_list = [(54, 2), (34, 55), (222, 23), (12, 45), (78, )]
K = int(input("Enter K: "))
print(Extract_tuple(Test_list, K))
