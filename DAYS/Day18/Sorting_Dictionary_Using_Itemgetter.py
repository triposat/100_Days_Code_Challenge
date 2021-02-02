from operator import itemgetter


def Sort_list_Name_and_Age(Test_list):
    Test_list.sort(key=itemgetter("Age", "Name"))
    return Test_list


def Sort_list_Age(Test_list):
    Test_list.sort(key=itemgetter('Age'))
    return Test_list


Test_list = [{"Name": "Tushar", "Age": 20},
             {"Name": "Aditya", "Age": 19},
             {"Name": "Satyam", "Age": 21}]
print(f"Age Sorting: {Sort_list_Age(Test_list)}")
print(f"Name and Age Sorting: {Sort_list_Name_and_Age(Test_list)}")
