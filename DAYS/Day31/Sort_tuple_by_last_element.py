def Sort_by_last_element(Test_tuple):
    return sorted(Test_tuple, key=lambda x: x[-1])


Test_tuple = [(1, 3), (3, 2), (2, 1)]
print(Sort_by_last_element(Test_tuple))
