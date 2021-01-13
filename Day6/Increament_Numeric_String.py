def Increment_Numeric_String(Test_list, n):
    Result = []
    for ele in Test_list:
        if ele.isdigit():
            Result.append(str(int(ele)+n))
        else:
            Result.append(ele)
    return Result


Given_list = ["100", "Days", "of", "CodeChallenge",
              "234", "is", "98", "123", "best", "4"]
n = 10
print(Increment_Numeric_String(Given_list, n))