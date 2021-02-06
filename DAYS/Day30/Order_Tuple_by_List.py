def Order_Tuple(Test_list, Ord_list):
    temp = dict(Test_list)
    return [(key, temp[key]) for key in Ord_list]


Test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
Ord_list = ['Geeks', 'best', 'CS', 'Gfg']
print(Order_Tuple(Test_list, Ord_list))
