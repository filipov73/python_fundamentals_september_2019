num = int(input())
word = input()
strings_list = []
search_strings_list = []

for _ in range(num):
    string = input()
    strings_list.append(string)
print(strings_list)
for st in strings_list:
    if word in st:
        search_strings_list.append(st)
print(search_strings_list)


# second code #
# for _ in range(num):
#     string = input()
#     strings_list.append(string)
# filter_strings_list = list(filter(lambda w: word in w, strings_list))
# print(strings_list)
# print(filter_strings_list)
