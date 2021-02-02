def Flatten_List(Given_List):
    stack = [Given_List]
    Result = []
    while stack:
        current = stack.pop(-1)
        if isinstance(current, list):
            stack.extend(current)
        else:
            Result.append(current)
    Result.reverse()
    return Result


Given_List = [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
print(f"Flatten list: {Flatten_List(Given_List)}")
