a = []
n = int(input("Enter the Number of Elements: "))
for i in range(0, n):
    element = int(input())
    a.append(element)
max = a[0]
min = a[0]
for i in range(1, n):
    if a[i] > max:
        max = a[i]
    if a[i] < min:
        min = a[i]
print(f"Max: {max}, MIN: {min}")
