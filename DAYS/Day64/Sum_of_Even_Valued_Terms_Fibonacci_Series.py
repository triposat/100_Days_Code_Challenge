def Even_Fib_Sum(limit):
    if limit < 2:
        return 0
    first = 1
    sec = 2
    sum = first+sec-1
    while sec <= limit:
        if first == 1:
            third = 4*sec+first-1
        else:
            third = 4*sec+first
        if third > limit:
            break
        first = sec
        sec = third
        sum = sum+sec
    return sum


# Driver Code
limit = int(input("Enter The Limit: "))
print(Even_Fib_Sum(limit))
