def Monotonic_List(Arr):
    return (all(Arr[i] <= Arr[i+1] for i in range(len(Arr)-1)) or all(Arr[i] >= Arr[i+1] for i in range(len(Arr)-1)))


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)
if Monotonic_List(a):
    print("Yup, It's an Monotonic List")
else:
    print("No, It's not an Monotonic List")
