string = "aaabbbbbcccccddd"
word = "abcc"
dict_string = {}
dict_word = {}

for s in set(string):
    dict_string[s] = string.count(s)

for s in set(word):
    dict_word[s] = word.count(s)

result = min([int(dict_string[s]/dict_word[s]) for s in set(word)])

print(result)


'''


'''