import string

def Mirror_Characters(Test_string, N):
    Test_Alpha = string.ascii_lowercase
    Test_Rever_Alpha = ''.join(list(reversed(Test_Alpha)))
    Dict_Alpha = dict(zip(Test_Alpha, Test_Rever_Alpha))
    Prefix = Test_string[:N-1]
    Suffix = Test_string[N-1:]
    Result = ""
    for elements in range(0, len(Test_string)):
        Result += Dict_Alpha[Test_string[elements]]
    return Result


Test_string = input("Enter a String: ")
n = int(input("N: "))
print(Mirror_Characters(Test_string, n))
