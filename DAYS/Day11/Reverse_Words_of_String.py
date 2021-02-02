def Word_Reverse(Test_String):
    return f"Reversed: {' '.join(reversed(Test_String.split(' ')))}"


Test_String = input("Enter a String: ")
print(Word_Reverse(Test_String))
