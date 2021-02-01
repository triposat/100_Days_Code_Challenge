def Unique_Values_Count(Test_dict):
    return {key: len(set([elements[key] for elements in Test_dict])) for key in Test_dict[0].keys()}


Test_dict = [{"Challenges": 1, "are": 3, "Best": 2}, {
    "Challenges": 1, "are": 3, "Best": 6}, {"Challenges": 7, "are": 3, "Best": 10}]
print(Unique_Values_Count(Test_dict))
