def Tranpose_Matrix(Check_list):
    Result = [[Check_list[i][j]
               for i in range(len(Check_list))] for j in range(len(Check_list[0]))]
    return Result


X = [[12, 7], [4, 5], [3, 8]]
Final = Tranpose_Matrix(X)
for items in Final:
    print(items)
