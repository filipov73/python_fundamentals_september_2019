st_1 = input()
st_2 = input()
st_out = ''
for i in range(len(st_1)):
    if st_1[i] != st_2[i]:
        st_out += st_2[i]
        print(st_out + st_1[i+1:])
    else:
        st_out += st_1[i]
