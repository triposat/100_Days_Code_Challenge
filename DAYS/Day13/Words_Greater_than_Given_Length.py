def Words_Greater_than_length(Test_string, length):
    return [words for words in Test_string.split() if len(words) > length]


Test_string = input("Enter a String: ")
length = int(input("Enter a Length: "))
print(*(Words_Greater_than_length(Test_string, length)))