text = input()

chars_dict = {}

for ch in text:
    if ch != " ":
        if ch in chars_dict:
            chars_dict[ch] += 1
        else:
            chars_dict[ch] = 1

for ch in chars_dict.items():
    print(f"{ch[0]} -> {ch[1]}")







# from collections import Counter
#
# text = input()
#
# chars_dict = Counter(text)
# chars_dict.pop(" ")
#
# for ch in chars_dict.items():
#     print(f"{ch[0]} -> {ch[1]}")
