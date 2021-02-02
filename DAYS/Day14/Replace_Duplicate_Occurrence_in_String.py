def Replace_Duplicates(Test_string, replace_dict):
    Test_list = Test_string.split()
    return [replace_dict.get(Value) if Value in replace_dict.keys() and Test_list.index(Value) != Index else Value for Index, Value in enumerate(Test_list)]


Test_string = 'Gfg is best . Gfg also has Classes now. Classes help understand better . '
replace_dict = {'Gfg':  'It', 'Classes': 'They'}
print(*(Replace_Duplicates(Test_string, replace_dict)))
