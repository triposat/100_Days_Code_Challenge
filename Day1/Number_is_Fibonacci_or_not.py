import math

def check_Perfect_Square(m):
    semifinal = int(math.sqrt(m))
    if pow(semifinal, 2) == m:
        return True
    return False


def fibo(n):
    t1 = 5*n*n+4
    t2 = 5*n*n-4
    if check_Perfect_Square(t1) or check_Perfect_Square(t2):
        return True
    else:
        return False


a = int(input("Enter a Number: "))
if fibo(a):
    print("Yup! It's a Fibinacci Number")
else:
    print("It's not a Fibonacci Number")
