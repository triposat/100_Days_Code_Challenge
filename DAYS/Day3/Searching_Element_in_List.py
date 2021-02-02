# Approach 1:

def Searching(Arr, ele):
    count = 0
    for i in Arr:
        if i == ele:
            print("Present")
            count = 1
            break
    if count == 0:
        print("Absent")


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)
b = int(input("Element to be Search: "))
Searching(a, b)

# Approach 2:

def Searching(Arr, ele):
    count = 0
    if  ele in Arr:
        print("Present")
    else:
        print("Absent")


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)
b = int(input("Element to be Search: "))
Searching(a, b)
