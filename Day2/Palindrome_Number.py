# Approach #1:

def Palindrome(a):
    result = 0
    temp = a
    while temp > 0:
        digit = temp % 10
        result = result*10+digit
        temp //= 10

    return "It's an Palindrome Number" if (result == a) else "No, It's not an Palindrome Number"


a = int(input("Enter a Number: "))
print(f"{Palindrome(a)}")

# Approach #2:

def Palindrome(a):
    b = "".join(reversed(str(a)))
    return "It's an Palindrome Number" if (int(b) == a) else "No, It's not an Palindrome Number"


a = int(input("Enter a Number: "))
print(f"{Palindrome(a)}")

# Approach #3:

def Palindrome(a):
    b = str(a)[::-1]
    return "It's an Palindrome Number" if (int(b) == a) else "No, It's not an Palindrome Number"


a = int(input("Enter a Number: "))
print(f"{Palindrome(a)}")
