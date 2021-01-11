def Remove_Empty_List(Given_List):
    Result = [ele for ele in Given_List if ele != []]
    return Result


Given_List = [5, 6, [], 7, 8, 9, [], 12, [], 4,[]]
print(Remove_Empty_List(Given_List))


Given_List = [5, 6, [], 7, 8, 9, [], 12, [], 4, []]
result = list(filter(None, Given_List))
print(result)

