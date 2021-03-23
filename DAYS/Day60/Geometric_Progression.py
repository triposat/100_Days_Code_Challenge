def Geometric(Test_list):
    ratio = Test_list[1]/Test_list[0]
    for ele in range(1, len(Test_list)-1):
        if not Test_list[ele+1]/Test_list[ele] == ratio:
            return False
    return True


if __name__ == "__main__":
    Test_list1 = [2, 6, 18, 54]
    Test_list2 = [10, 5, 2.5, 1.25]
    Test_list3 = [5, 8, 9, 11]
    print(Geometric(Test_list1))
    print(Geometric(Test_list2))
    print(Geometric(Test_list3))
