string_list = input().split(" ")

new_string_list = []

for word in string_list:
    num_str = ""
    for ch in word:
        if ch.isdigit():
            num_str += ch

    new_string = word.replace(num_str, chr(int(num_str)))
    st = list(new_string)
    st[1], st[-1] = st[-1], st[1]
    new_string = "".join(st)
    new_string_list.append(new_string)

print(" ".join(new_string_list))
