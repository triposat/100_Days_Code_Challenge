def Anagram(Test_list):
    Dict = {}
    for elements in Test_list:
        Key = ''.join(sorted(elements))
        if Key in Dict.keys():
            Dict[Key].append(elements)
        else:
            Dict[Key] = []
            Dict[Key].append(elements)
    Result=""
    for keys, values in Dict.items():
        Result+=' '.join(values)+" "
    return Result



if __name__ == "__main__":
    Test_list = ['cat', 'dog', 'tac', 'god', 'act']
    print(Anagram(Test_list))
