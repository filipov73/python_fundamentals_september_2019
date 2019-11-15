string = input().split(", ")

for st in string:
    if 3 <= len(st) <= 16:
        if (st.isalnum() and "@" not in st) or "_" in st or "-" in st:
            print(st)
