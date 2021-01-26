def Sort_Dictionary(Test_list):
    return sorted(Test_list, key=lambda dic: dic["Age"])


Test_list = [{"Name": "Satyam", "Age": 20},
             {"Name": "Aditya", "Age": 20},
             {"Name": "Tushar", "Age": 19}]
print(Sort_Dictionary(Test_list))