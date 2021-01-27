def Sort_Keys_and_Values(Test_dict):
    return {key: sorted(Test_dict[key]) for key in sorted(Test_dict)}


Test_dict = {'Code': [7, 6, 3],
             'Challenge': [2, 10, 3],
             'is': [19, 4], 'Best': [18, 20, 7]}
print(Sort_Keys_and_Values(Test_dict))
