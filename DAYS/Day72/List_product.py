def List_prod(Test_list):
    Result = []
    for i in Test_list:
        product = 1
        for j in Test_list:
            if j != i:
                product *= j
        Result.append(product)
    return Result


if __name__ == "__main__":
    print(List_prod([10, 20, 30, 40, 50]))
    print(List_prod([1, 2, 0, 4]))
    print(List_prod([1, 2, 3, -4]))
