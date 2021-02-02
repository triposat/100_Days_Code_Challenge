def Words_Pair(Test_list):
    count = 0
    reverse_words = []
    for word in Test_list:
        if word[::-1] in Test_list:
            Test_list.remove(word[::-1])
            Test_list.remove(word)
            count += 1
    return count


Given_list = ["skeeg", "best", "tseb",
              "for", "skeeg", "skeeg", "best", "geeks", "tseb"]
print(Words_Pair(Given_list))
