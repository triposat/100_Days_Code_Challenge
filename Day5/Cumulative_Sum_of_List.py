def Cumulative_Sum(Given_List):
    Result = []
    sum = 0
    for i in range(0, len(Given_List)):
        sum += Given_List[i]
        Result.append(sum)
    return Result


Given_List = [10, 20, 30, 40, 50, 60]
print(Cumulative_Sum(Given_List))
