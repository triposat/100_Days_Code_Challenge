def encode(Test_string):
    count = 0
    Result = ""
    for i in range(len(Test_string)):
        if (i+1) < len(Test_string) and (Test_string[i] == Test_string[i+1]):
            count += 1
        else:
            Result += str((count+1))+Test_string[i]
            count = 0
    return Result


print(encode("ABBBBCCCCCCCCAB"))