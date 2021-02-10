def Linear_Search(Test_list, k):
        for ele in range(len(Test_list)):
            if Test_list[ele] == k:
                return ele

        return -1


Test_list = [2, 3, 4, 10, 40]
k = int(input("Which Element: "))
Result = Linear_Search(Test_list, k)
if Result != -1:
    print(f"Found at {Result}")
else:
    print(f"Not Found")
