def Values_Sum_Greater(Test_Dict):
    return sum(list(Test_Dict.keys())) < sum(list(Test_Dict.values()))


Test_Dict = {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}
print(Values_Sum_Greater(Test_Dict))
