def Find_triplets(Test_list, length):
    found = False
    for i in range(0, length-1):
        s = set()
        for j in range(i+1, length):
            Add = -(Test_list[i]+Test_list[j])
            if Add in s:
                print(list(sorted([Add, Test_list[i], Test_list[j]])))
                found = True
            else:
                s.add(Test_list[j])
    if not found:
        print("No Triplets Found")


Test_list = [-25, -10, -7, -3, 2, 4, 8, 10]
Find_triplets(Test_list, len(Test_list))
