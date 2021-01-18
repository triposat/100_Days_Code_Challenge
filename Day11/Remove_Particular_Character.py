# Approach 1:

def Word_Reverse(Test_String, Test_Word):
    Final_String = ""
    for words in Test_String:
        if words != Test_Word:
            Final_String += words
    return Final_String


Test_String = input("Enter a String: ")
Test_Word = input("Enter a Word: ")
print(Word_Reverse(Test_String, Test_Word))

# Approach 2:

def Word_Reverse(Test_String, Test_Word):
    return ''.join([ele for ele in Test_String if ele != Test_Word])


Test_String = input("Enter a String: ")
Test_Word = input("Enter a Word: ")
print(Word_Reverse(Test_String, Test_Word))
