# Approach 1:

def Second_Largest(Arr):
    Arr.remove(max(Arr))
    return max(Arr)


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(f"Second Largest: {Second_Largest(a)}")

# Approach 2:

def Second_Largest(Arr):
    return sorted(Arr)[-2]


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(f"Second Largest: {Second_Largest(a)}")
