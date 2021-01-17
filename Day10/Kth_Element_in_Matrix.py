# Approach 1:

def Kth_Element(Test_list, k):
    return [ele[k-1] for ele in Test_list]


Test_list = [[4, 5, 6],
             [8, 1, 10],
             [7, 12, 5]]
k = 2
print(Kth_Element(Test_list, k))

# Approach 2:


def Kth_Element(Test_list, k):
    Result = list(zip(*Test_list))[k-1]
    return Result


Test_list = [[4, 5, 6],
             [8, 1, 10],
             [7, 12, 5]]
k = 2
print(list(Kth_Element(Test_list, k)))
