# Approach 1:

def Swap_Last_with_First(Arr):
    temp = Arr[0]
    Arr[0] = Arr[len(Arr)-1]
    Arr[len(Arr)-1] = temp
    return Arr


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(f"List After Swapping: {Swap_Last_with_First(a)}")

# Approach 2:

def Swap_Last_with_First(Arr):
    Arr[0], Arr[-1] = Arr[-1], Arr[0]
    return Arr


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(f"List After Swapping: {Swap_Last_with_First(a)}")
