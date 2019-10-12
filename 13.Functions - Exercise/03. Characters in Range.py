def between_strings(s_1, s_2):
    res_list = []
    s1, s2 = ord(st_1), ord(st_2)
    for x in range(s1+1, s2):
        res_list.append(x)
    return res_list


st_1 = input()
st_2 = input()
res = between_strings(st_1, st_2)
print(" ".join(map(chr, res)))
