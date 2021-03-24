def is_anagram(str1, str2):
    first = list(str1)
    first.sort()
    second = list(str2)
    second.sort()
    return first == second


print(is_anagram('anagram', 'nagaram'))
print(is_anagram('cat', 'rat'))
print(is_anagram('education', 'uaconitde'))
