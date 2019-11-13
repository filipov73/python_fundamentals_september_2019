change_word_list = input().split(", ")
text = input()

for word in change_word_list:
    length = len(word)
    text = text.replace(word, "*" * length)
print(text)
