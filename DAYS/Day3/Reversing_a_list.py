# Approach 1:

def Reversing(Arr):
    return [ele for ele in reversed(Arr)]


a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(f"Reversed List: {Reversing(a)}")

# Approach 2:

def Reversing(Arr):
    return Arr[::-1]

a = []
n = int(input("How Many Elements: "))
print("Enter The Elements: ")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(f"Reversed List: {Reversing(a)}")
