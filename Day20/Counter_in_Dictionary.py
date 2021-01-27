from collections import Counter


def Counter_Dict(Test_list):
    Dict = Counter(Test_list)
    Maximum = max(Dict.values())
    return sorted([ele for ele in Dict.keys() if Dict[ele] == Maximum])[0]


Test_list = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie',
             'jamie', 'jamie', 'john', 'johnny', 'jamie', 'johnny', 'john']
print(Counter_Dict(Test_list))