def Sort_by_Last_Name(Test_list):
    Test_list.sort(key=lambda names: names.split()[-1])
    return Test_list


Test_list = ['John Wick', 'Jason Voorhees', 'Freddy Krueger',
             'Keyser Soze', 'Mohinder Singh Pandher']
print(Sort_by_Last_Name(Test_list))
