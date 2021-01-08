def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if(greater % a == 0) and (greater % b == 0):
            result = greater
            break
        else:
            greater += 1
    return result


a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
print(f"LCM of {a} and {b}: {lcm(a,b)}")
