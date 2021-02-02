def Dict_to_List(Test_dict):
    Result = [[key]*value for key, value in Test_dict.items()]
    return [items for elements in Result for items in elements]


Test_dict = {'S': 2, 'a': 3, 'm': 1, 't': 4, 'y': 1, 'y': 4, 't': 3}
print(Dict_to_List(Test_dict))
