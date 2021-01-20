def Replace_Multiple_Words(Test_string, Word_list, Replace_word):
    return " ".join([Replace_word if words in Word_list else words for words in Test_string.split()])


Test_string = "Geeksforgeeks is best for geeks and CS"
Word_list = ["best", 'CS', 'for']
Replace_word = 'gfg'
print(Replace_Multiple_Words(Test_string, Word_list, Replace_word))
