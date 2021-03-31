def Difference(num):
    first = range(1, num+1)
    square_of_sum = sum(first)
    return (square_of_sum*square_of_sum - sum(i*i for i in first))


if __name__ == "__main__":
    num = int(input("Enter Upper Limit: "))
    print(Difference(num))
