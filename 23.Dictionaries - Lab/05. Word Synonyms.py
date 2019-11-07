number = int(input())

synonyms_dict = {}

for _ in range(number):
    word = input()
    synonym = input()
    if word not in synonyms_dict:
        synonyms_dict[word] = [synonym]
    else:
        synonyms_dict[word].append(synonym)

for key, list_ in synonyms_dict.items():
    print(f"{key} - ", end="")
    print(", ".join(list_))
