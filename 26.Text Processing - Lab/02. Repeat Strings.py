words_list = input().split()

for word in words_list:
    char_len = len(word)
    print(word * char_len, end="")
