def String_with_Vowels(Test_string):
    return all([words in "aeiouAEIOU" for words in Test_string])


Test_string = input("Enter a String: ")
if String_with_Vowels(Test_string):
    print("Accepted")
else:
    print("Not Accepted")
