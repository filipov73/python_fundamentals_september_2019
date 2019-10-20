electrons = int(input())
e_list = []
while electrons:
    index = len(e_list) + 1
    el = 2*index**2
    if electrons <= el:
        el = electrons
    e_list.append(el)
    electrons -= el
print(e_list)
