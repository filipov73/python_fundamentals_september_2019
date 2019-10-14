# 05. The Office

happiness_list = list(map(int, input().split(" ")))
happiness_percent = int(input())
happiness_list_with_percent = [x * happiness_percent for x in happiness_list]
average_happiness = sum(happiness_list_with_percent) / len(happiness_list_with_percent)
filtered_happiness_list = list(filter(lambda x: x >= average_happiness, happiness_list_with_percent))
if len(happiness_list) / 2 > len(filtered_happiness_list):
    print(f"Score: {len(filtered_happiness_list)}/{len(happiness_list)}. Employees are not happy!")
else:
    print(f"Score: {len(filtered_happiness_list)}/{len(happiness_list)}. Employees are happy!")


# 04. Even Numbers

# string_list = list(map(int, input().split(", ")))
# res = []
# for num in string_list:
#     if num % 2 == 0:
#         res.append(string_list.index(num))
# print(res)


# string_list = list(map(int, input().split(", ")))
# res = []
# for idx, num in enumerate(string_list):
#     if num % 2 == 0:
#         res.append(idx)
# print(res)


# 03. Palindrome Strings

string_list = input().split(" ")
search_word = input()

print([s for s in string_list if s == s[::-1]])
print(f"Found palindrome {string_list.count(search_word)} times")


# 02. Todo List

# note = input()
# notes_list = [None] * 10
# while note != "End":
#     note = note.split("-")
#     idx = int(note[0])
#     text = note[1]
#     notes_list.insert(idx, text)
#     note = input()
# print(list(filter(lambda x: x != None, notes_list)))


# 1 Submit a solution

# train_list = [0] * int(input())
# command = input().split(" ")
# while command[0] != "End":
#     if command[0] == "add":
#         people = int(command[1])
#         train_list[-1] += people
#     elif command[0] == "insert":
#         idx = int(command[1])
#         people = int(command[2])
#         train_list[idx] += people
#     elif command[0] == "leave":
#         idx = int(command[1])
#         people = int(command[2])
#         train_list[idx] -= people
#
#     command = input().split()
# print(train_list)
