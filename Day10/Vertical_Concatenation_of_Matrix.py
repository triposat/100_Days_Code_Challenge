def Vertical_Concatenation(Test_list):
    Result = []
    n = 0
    while n != len(Test_list):
        temp = ''
        for indexes in Test_list:
            try:
                temp += indexes[n]
            except IndexError:
                pass
        n += 1
        Result.append(temp)
    return Result


Test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
print(Vertical_Concatenation(Test_list))