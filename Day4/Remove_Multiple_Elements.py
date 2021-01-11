# Approach 1:

def Remove_Multiple(Arr1, Arr2):
    Final = [ele for ele in Arr1 if ele not in Arr2]
    return Final


a = [1, 2, 3, 4, 5]
b = [3, 4]
print(Remove_Multiple(a, b))

# Approach 2:

def Remove_Multiple(Arr1, Arr2):
    for ele in Arr2:
        Arr1.remove(ele)
    return Arr1


a = [1, 2, 3, 4, 5]
b = [3, 4]
print(Remove_Multiple(a, b))
