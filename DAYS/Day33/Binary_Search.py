def Binary_Search(Test_list, low, high, k):
    if high >= low:
        Mid = (low+high)//2
        if Test_list[Mid] == k:
            return Mid
        elif Test_list[Mid] > k:
            return Binary_Search(Test_list, low, Mid-1, k)
        else:
            return Binary_Search(Test_list, Mid+1, high, k)
    else:
        return -1


Test_list = [2, 3, 4, 10, 40]
k = int(input("Which Element: "))
Result = Binary_Search(Test_list, 0, len(Test_list)-1, k)
if Result != -1:
    print(f"Found at {Result}")
else:
    print(f"Not Found")
