def Rotate_Dict(Test_Dict, K):
    Test_Dict = list(Test_Dict.items())
    c = Test_Dict[len(Test_Dict)-K:]+Test_Dict[:-K]
    return {sub[0]: sub[1] for sub in c}


Test_Dict = {1: 6, 8: 1, 9: 3, 10: 8, 12: 6, 4: 9}
K = int(input("Enter K: "))
print(Rotate_Dict(Test_Dict, K))
