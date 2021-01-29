def Counting_the_frequency(Test_list):
    Test_dict = {}
    for items in Test_list:
        Test_dict[items] = Test_list.count(items)
    for key, value in Test_dict.items():
        print(f"{key} : {value}")


Test_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
Counting_the_frequency(Test_list)