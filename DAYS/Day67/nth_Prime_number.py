def nth_Prime(num):
    Semi = num*num
    Res_1 = [True for i in range(Semi+1)]
    prime = 2
    while prime*prime <= Semi:
        if Res_1[prime] == True:
            for i in range(prime*prime, Semi+1, prime):
                Res_1[i] = False
        prime += 1
    Res_2 = []
    for i in range(2, Semi+1):
        if Res_1[i]:
            Res_2.append(i)
    return Res_2[num-1]


if __name__ == "__main__":
    num = int(input("Enter nth Number: "))
    print(nth_Prime(num))
