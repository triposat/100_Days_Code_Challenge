def Generate_gray(bits):
    hey = ["0", "1"]
    hey1, hey2 = [], []
    if bits <= 0:
        return ["0"]
    if bits == 1:
        return ["0", "1"]
    while bits != 1:
        hey1, hey2 = [], []
        for i in range(len(hey)):
            hey1.append("0"+hey[i])
        for i in range(len(hey)):
            hey2.append("1"+hey[i])
        hey = []
        hey = hey1+hey2
        bits -= 1
    return hey


if __name__ == "__main__":
    bits = int(input("How many Bits: "))
    Res = Generate_gray(bits)
    for code in Res:
        print("  ".join(code))
