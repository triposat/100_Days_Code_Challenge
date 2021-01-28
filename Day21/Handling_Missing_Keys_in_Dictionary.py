from collections import defaultdict
Test_dict = defaultdict(lambda: "Key Not Found")
Test_dict['a'] = 1
Test_dict['b'] = 2
print(Test_dict['d'])
print(Test_dict['a'])
