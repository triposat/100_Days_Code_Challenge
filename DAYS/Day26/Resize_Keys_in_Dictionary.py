def Resize_Dict(Test_Dict, K):
    return {key[:k]: Test_Dict[key] for key in Test_Dict}


Test_Dict = {"geeksforgeeks": 3, "best": 3, "coding": 4, "practice": 3}
k = int(input("Enter K: "))
print(Resize_Dict(Test_Dict, k))
