def Valid_string(first, second, remain):
    Sum_str = str(int(first)+int(second))
    if Sum_str == remain:
        return True
    elif remain.startswith(Sum_str):
        return Valid_string(second, Sum_str, remain[len(Sum_str):])
    else:
        return False


def Additive_Sequence(Test_string):
    length = len(Test_string)
    for i in range(1, int(length/2)+1):
        for j in range(1, int(length-i/2)+1):  # int(length/2)
            first, second, remain = Test_string[:i], Test_string[i:i +
                                                                 j], Test_string[i+j:]
            if Valid_string(first, second, remain):
                return True
    return False


if __name__ == "__main__":
    Test_string = input("Enter String of Numbers: ")
    print(Additive_Sequence(Test_string))
