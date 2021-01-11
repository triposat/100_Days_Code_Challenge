def N_Largest_Elements(Arr, Upto):
    result = []
    for i in range(0, Upto):
        max = 0
        for j in range(0, len(Arr)):
            if Arr[j] > max:
                max = Arr[j]
        Arr.remove(max)
        result.append(max)
    return result


Given_List = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    Given_List.append(element)
Upto = int(input("Upto Which Number: "))
print(N_Largest_Elements(Given_List, Upto))








def N_Largest_Elemnts(Arr, Upto):
    return sorted(Arr)[-Upto:]


    Given_List = []
    n = int(input("How Many Elements: "))
    print("Enter The Elements: ")
    for i in range(0, n):
        element = int(input())
        Given_List.append(element)
    Upto = int(input("Upto Which Number: "))
    print(N_Largest_Elemnts(Given_List, Upto))
