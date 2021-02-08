def Remove_Elements(Test_list):
    return [sub for sub in Test_list if not all(ele == None for ele in sub)]


Test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
print(Remove_Elements(Test_list))
