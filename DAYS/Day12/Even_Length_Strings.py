def Even_Length(Test_string):
    return "\n".join([words for words in Test_string.split() if len(words) % 2 == 0])


Test_string = input("Enter a String: ")
print(f"Output: {Even_Length(Test_string)}")