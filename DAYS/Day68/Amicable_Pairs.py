def sum_factors(num):
    Result = []
    for i in range(1, num):
        if num % i == 0:
            Result.append(i)
    return sum(Result)


def amicable_pairs(num):
    Result1 = []
    Result2 = []

    for x in range(1, num+1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            Result1.append(tuple(sorted((x, y))))
            Result2.append(x+y)

        x += 1
    return set(Result1), sum(set(Result2))


if __name__ == "__main__":
    num = int(input("Enter n: "))
    a, b = amicable_pairs(num)
    print(f"Amicable Pairs: {a}")
    print(f"Sum of Amicable Pairs: {b}")
