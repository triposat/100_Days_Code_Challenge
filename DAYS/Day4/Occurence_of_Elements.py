# Approach 1:

def Occurence_of_Element(Given_List, Element):
    count = 0
    for ele in Given_List:
        if ele == Element:
            count += 1
    return count


Given_List = [14, 25, 16, 23, 10, 5, 6, 8, 7, 9, 10, 25, 14]
Element = 14
print(Occurence_of_Element(Given_List, Element))

# Approach 2:

def Occurence_of_Element(Given_List, Element):
    return Given_List.count(Element)


Given_List = [14, 25, 16, 23, 10, 5, 6, 8, 7, 9, 10, 25, 14]
Element = 14
print(Occurence_of_Element(Given_List, Element))
