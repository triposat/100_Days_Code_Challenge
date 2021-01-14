def Remove_Specific_Digit(Test_list, n):
    Result = []
    for ele in Test_list:
        Result.append(''.join([elem for elem in str(ele) if int(elem) != n]))
    return list(filter(None, Result))


Test_list = [343, 893, 1948, 3433333, 2346]
n = int(input("Specific Character: "))
print(Remove_Specific_Digit(Test_list, n))
