names = input().split(" ")
command = input()

while command != "Export":
    tokens = command.split(" ")
    if tokens[0] == "Add":
        contact = tokens[1]
        idx = int(tokens[2])
        if contact in names:
            if 0 <= idx < len(names):
                names.insert(idx, contact)
        else:
            names.append(contact)
    elif tokens[0] == "Remove":
        idx = int(tokens[1])
        if 0 <= idx < len(names):
            names.pop(idx)
    elif tokens[0] == "Export":
        star_idx = int(tokens[1])
        count = int(tokens[2])
        if count > len(names) - star_idx:
            count = len(names) - star_idx
        print(" ".join([x for i, x in enumerate(names) if i in range(star_idx, star_idx + count)]))
    elif tokens[0] == "Print":
        nor_rev = tokens[1]
        if nor_rev == "Normal":
            print(f"Contacts: " + " ".join(names))
            break
        else:
            print(f"Contacts: " + " ".join(reversed(names)))
            break
    command = input()
