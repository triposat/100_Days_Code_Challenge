def hcf(a, b):
    if a < b:
        small = a
    else:
        small = b
    for i in range(1, small + 1):
        print(i)
        if (a % i == 0) and (b % i == 0):
            hcf = i
    return hcf


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
print(f"HCF: {hcf(a,b)}")
