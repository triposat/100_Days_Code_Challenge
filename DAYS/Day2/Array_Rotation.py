# Approach #1:  

a, b = [], []
n = int(input("Enter the Number of Elements: "))
for i in range(0, n):
    element = int(input())
    a.append(element)

c = int(input("From Which: "))
b.append(a[:c])
d = [k for k in a if k not in b[0]]
d.extend(b[0])
print(d)

# Approach #2: 

def Array_Rotate(arr, n):
    for i in range(0, n):
        first = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = first

    print(arr)


a, b = [], []
n = int(input("Enter the Number of Elements: "))
for i in range(0, n):
    element = int(input())
    a.append(element)
c = int(input("From Which: "))
Array_Rotate(a, c)
