def Break_Chunks(Given_List, n):
    return [Given_List[ele:ele+n] for ele in range(1, len(Given_List), n)]


Given_List = [10, 45, 20, 62, 47, 85, 12, 63, 24, 78, 10]
n = 2
print(Break_Chunks(Given_List, n))
