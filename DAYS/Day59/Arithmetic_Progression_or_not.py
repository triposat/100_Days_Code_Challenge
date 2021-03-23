def Arithmetic_Prog(Test_list):
    first = Test_list[1]-Test_list[0]
    for ele in range(len(Test_list)-1):
        if not Test_list[ele+1]-Test_list[ele] == first:
            return False
    return True


if __name__ == "__main__":
    Test_list1 = [5, 7, 9, 11]
    Test_list2 = [5, 8, 9, 11]
    print(Arithmetic_Prog(Test_list1))
    print(Arithmetic_Prog(Test_list2))
