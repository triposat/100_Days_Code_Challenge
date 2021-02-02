from itertools import permutations


def Permutation_of_String(Test_string):
    Perm_list = permutations(Test_string)
    return "\n".join(["".join(perms) for perms in list(Perm_list)])


Test_string = input("Enter a String: ")
print(Permutation_of_String(Test_string))
