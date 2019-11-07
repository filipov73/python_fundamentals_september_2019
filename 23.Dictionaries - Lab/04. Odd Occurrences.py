from collections import Counter

words = input().lower().split(" ")

words_dict = Counter(words)
print(" ".join([item[0] for item in words_dict.items() if item[1] % 2 == 1]))

# words_dict = {}
# for word in words:
#     if word in words_dict:
#         words_dict[word] += 1
#     else:
#         words_dict[word] = 1

# print(" ".join([item[0] for item in words_dict.items() if item[1] % 2 == 1]))

