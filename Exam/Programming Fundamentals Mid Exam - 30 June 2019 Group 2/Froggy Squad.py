names = input().split(" ")
# command = input()

while True:
    command = input().split(" ")
    if command[0] == "Join":
        name = command[1]
        if name not in names:
            names.append(name)
    elif command[0] == "Jump":
        name = command[1]
        idx = int(command[2])
        if 0 <= idx < len(names):
            names.insert(idx, name)
    elif command[0] == "Dive":
        idx = int(command[1])
        if 0 <= idx < len(names):
            names.pop(idx)
    elif command[0] == "First":
        count = int(command[1])
        print(" ".join(names[:count]))
    elif command[0] == "Last":
        count = int(command[1])
        print(" ".join(names[-count:]))
    elif command[0] == "Print":
        nor_rev = command[1]
        if nor_rev == "Normal":
            print("Frogs: " + " ".join(names))
            break
        elif nor_rev == "Reversed":
            print("Frogs: " + " ".join(reversed(names)))
            break
