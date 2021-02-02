def Remove_ith_Character(Test_string, Character):
    return Test_string[:Character]+Test_string[Character+1:]


Test_string = input("Enter a String: ")
Character = int(input("Enter ith Character: "))
print(Remove_ith_Character(Test_string, Character))