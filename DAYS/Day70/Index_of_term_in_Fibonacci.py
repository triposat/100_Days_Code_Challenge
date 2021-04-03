import itertools


def Fibo_index(num):
    Prev_term = 0
    Curr_term = 1
    for i in itertools.count(1):
        if len(str(Curr_term)) == num:
            return i, Curr_term
        Prev_term, Curr_term = Curr_term, Prev_term+Curr_term


if __name__ == "__main__":
    num = int(input("Enter n: "))
    Index, number = Fibo_index(num)
    print(f"Number is {number}")
    print(f"Index is: {Index}")
