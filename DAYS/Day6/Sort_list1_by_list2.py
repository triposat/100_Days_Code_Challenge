def Sort_One_by_Other(Arr1, Arr2):
    Result = zip(Arr2, Arr1)
    Result = [ele for _, ele in sorted(Result)]
    print(Result)


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
Sort_One_by_Other(x, y)
