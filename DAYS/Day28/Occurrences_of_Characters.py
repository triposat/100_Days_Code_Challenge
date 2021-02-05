def encode(Test_string):
    count = 1
    Result = ""
    for i in range(len(Test_string)):
        if (i+1) < len(Test_string) and (Test_string[i] == Test_string[i+1]):
            count += 1
        else:
            Result += str(count)+Test_string[i]
            count = 1
    return Result


print(encode("ABBBBCCCCCCCCAB"))
