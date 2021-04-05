def Z_print(Test_list):
    Result = []
    diff = len(Test_list)-len(Test_list[0])
    for i in range(len(Test_list)):
        if i == 0 or i == len(Test_list)-1:
            Result.append(Test_list[i])
            Result = Result[0]
            print(*Result)
            Result = []
        else:
            Result.append(Test_list[i][len(Test_list)-i-1-diff])
            a = Result[0]
            print("  " * (len(Test_list)-i-1-diff) + str(a))
            Result = []

    return Result


if __name__ == "__main__":
    Test_list1 = [[4, 5, 6, 8, 5],
                  [1, 2, 3, 1, 4],
                  [7, 8, 9, 4, 7],
                  [1, 8, 7, 5, 2],
                  [7, 9, 5, 6, 9],
                  [9, 4, 5, 6, 6]]
    Test_list2 = [[4, 5, 6, 8],
                  [1, 2, 3, 1],
                  [7, 8, 9, 4],
                  [1, 8, 7, 5]]
    print("1st: ")
    Z_print(Test_list1)
    print("\n")
    print("2nd: ")
    Z_print(Test_list2)
