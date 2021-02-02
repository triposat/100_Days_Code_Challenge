def Filter_Dictionaries(Test_list, Search_list, Element):
    return [Sub_dict for Sub_dict in Test_list if Sub_dict[Element] in Search_list]


Test_list = [{"Gfg": 3, "is": 5, "best": 10},
             {"Gfg": 5, "is": 1, "best": 1},
             {"Gfg": 8, "is": 3, "best": 9},
             {"Gfg": 9, "is": 9, "best": 8},
             {"Gfg": 4, "is": 10, "best": 7}]

Search_list = [1, 9, 8, 4, 5]
Element = "best"
print(Filter_Dictionaries(Test_list, Search_list, Element))
