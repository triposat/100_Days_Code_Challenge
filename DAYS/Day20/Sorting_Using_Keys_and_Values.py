def Sorting_by_Keys(Key_Values):
    return {key: value for key, value in sorted(Key_Values.items())}


def Sorting_by_Values(Key_Values):
    return {key: value for key, value in sorted(Key_Values.items(), key=lambda elements: elements[1])}


Key_Values = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
print(f"Sorting by Keys: {Sorting_by_Keys(Key_Values)}")
print(f"Sorting by Values: {Sorting_by_Values(Key_Values)}")


# from operator import itemgetter
# def Sorting_by_Values(Key_Values):
#     return {key: value for key, value in sorted(Key_Values.items(), key=itemgetter(1))}


# Key_Values = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
# print(Sorting_by_Values(Key_Values))
