def Remove_Tuple(Test_list, K):
    return [elements for elements in Test_list if len(elements) != K]


Test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K = int(input("Enter K: "))
print(Remove_Tuple(Test_list, K))
