first_list = input().split(", ")
second_list = input().split(", ")

res_list = []

for st_1 in first_list:
    for st_2 in second_list:
        if st_1 in st_2:
            res_list.append(st_1)
print(sorted(set(res_list), key=res_list.index))
