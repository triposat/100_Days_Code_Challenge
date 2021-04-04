def Intinerary(Test_list, start):
    Result = [start]
    while len(Test_list) >= 1:
        Semi_dict = {}
        for i in Test_list:
            if i[0] == start:
                Semi_dict[i[0]] = i[1]
        try:
            current = min(Semi_dict.values())
            Test_list.remove((start, current))
            Result.append(current)
            start = current
        except:
            return "Invalid intinerary, Unable to process..."
    return Result


if __name__ == "__main__":
    Test_list1 = [('SFO', 'HKO'), ('YYZ', 'SFO'),
                  ('YUL', 'YYZ'), ('HKO', 'ORD')]
    start1 = 'YUL'

    Test_list2 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    start2 = 'A'

    Test_list3 = [('SFO', 'COM'), ('COM', 'YYZ')]
    start3 = 'COM'
    print(Intinerary(Test_list1, start1))
    print(Intinerary(Test_list2, start2))
    print(Intinerary(Test_list3, start3))
