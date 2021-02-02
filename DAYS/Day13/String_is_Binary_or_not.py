def Binary_or_not(Test_string):
    Binary = "01"
    return all([numbers in Binary for numbers in Test_string])


Test_string = input("Enter a String: ")
if Binary_or_not(Test_string):
    print("Binary")
else:
    print("Not a Binary")
