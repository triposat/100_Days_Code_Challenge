def Find_Duplicates(Given_List):
    Duplicates = []
    for i in range(0, len(Given_List)):
        for j in range(i+1, len(Given_List)):
            if Given_List[i] == Given_List[j] and Given_List[i] not in Duplicates:
                Duplicates.append(Given_List[i])
    return Duplicates


Given_List = [4, 5, 1, 2, 6, 5, 2]
print(Find_Duplicates(Given_List))
