def Snake_to_Pascal(Test_String):
    return Test_String.replace("_", " ").title().replace(" ", "")


Test_String = input("Enter a String: ")
print(Snake_to_Pascal(Test_String))