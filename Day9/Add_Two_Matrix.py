def Add_Matrix(X, Y):
    return [X[i][j]+Y[i][j] for i in range(len(X)) for j in range(len(X[0]))]


X = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
print(Add_Matrix(X, Y))
