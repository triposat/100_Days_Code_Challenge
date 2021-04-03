import string


def letter_string(Test_string):
    digs = ""
    letters = ""
    Result = ""
    for i in Test_string:
        if i in string.digits:
            digs += i
        else:
            letters += i
    for index,  num in enumerate(digs):
        Result += int(num)*letters[index]
    return Result


if __name__ == "__main__":
    Test_string = input("Enter String: ")
    print(letter_string(Test_string))
