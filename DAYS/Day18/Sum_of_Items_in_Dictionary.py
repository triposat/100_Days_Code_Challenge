def Sum_of_Values(Test_dict):
    count = 0
    for ele in Test_dict.values():
        count += ele
    return count


Test_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
print(f'Total Sum: {Sum_of_Values(Test_dict)}')
