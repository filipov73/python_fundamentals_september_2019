string_list = list(map(int, input().split(", ")))
res = []
for num in string_list:
    if num % 2 == 0:
        res.append(string_list.index(num))
print(res)


# string_list = list(map(int, input().split(", ")))
# res = []
# for idx, num in enumerate(string_list):
#     if num % 2 == 0:
#         res.append(idx)
# print(res)