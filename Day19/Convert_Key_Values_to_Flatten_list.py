def Convert_Dict(Test_dict):
    return dict(zip(Test_dict['Month'], Test_dict['Name']))


Test_dict = {'Month': [1, 2, 3],
             'Name': ['Jan', 'Feb', 'March']}
print(Convert_Dict(Test_dict))
