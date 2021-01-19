def Least_Frequency(Test_string):
    Result = {}
    for words in Test_string:
        if words in Result:
            Result[words] += 1
        else:
            Result[words] = 1
    Final_Result = min(Result, key=Result.get)
    return Final_Result


Test_string = input("Enter a String: ")
print(Least_Frequency(Test_string))