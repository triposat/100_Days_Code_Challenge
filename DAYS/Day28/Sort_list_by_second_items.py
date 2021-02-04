# Approach 1:

from operator import itemgetter


def Sort_by_second_items(Test_tup):
    Test_tup.sort(key=lambda x: x[1])
    return Test_tup


Test_tup = [('for', 24), ('is', 10), ('Geeks', 28),
            ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
print(Sort_by_second_items(Test_tup))

# Approach 2:


def Sort_by_second_items(Test_tup):
    Test_tup.sort(key=itemgetter(1))
    return Test_tup


Test_tup = [('for', 24), ('is', 10), ('Geeks', 28),
            ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
print(Sort_by_second_items(Test_tup))
