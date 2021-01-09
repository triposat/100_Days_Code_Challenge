def Armstrong(a):
    temp = a
    result = 0
    order = len(str(a))
    while temp > 0:
        digit = temp % 10
        result += digit**order
        temp //= 10
    return "It's an Armstrong Number" if (result == a) else "No, It's not an Armstrong Number"


a = int(input("Enter a Number: "))
print(f"{Armstrong(a)}")
