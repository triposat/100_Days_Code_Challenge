def Extract_Dictionary_Values(Test_dict):
    return [sorted({numbers for ele in Test_dict.values() for numbers in ele})]


Test_dict = {'Challenges': [5, 6, 7, 8],
             'are': [10, 11, 7, 5],
             'best': [6, 12, 10, 8],
             'for': [1, 2, 5]}
print(*(Extract_Dictionary_Values(Test_dict)))
