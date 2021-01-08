def fibo(a):
    m, n = 0, 1
    count = 0
    if a <= 0:
        print("Alert! Wrong Input")
    elif a == 1:
        print(f"Fibonacci Series: {m}")
    else:
        print(f"Fibonacci Series: ", end="")
        while count < a:
            count += 1
            print(m, end=" ")
            nth = m+n
            m = n
            n = nth

a = int(input("How Many Terms do you want to Display: "))
fibo(a)
