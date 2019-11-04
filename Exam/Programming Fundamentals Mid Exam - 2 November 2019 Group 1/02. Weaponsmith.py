weapons = input().split("|")

command = input()

while command != "Done":
    tokens = command.split(" ")
    if tokens[0] == "Move":
        move = tokens[1]
        idx = int(tokens[2])
        if 0 <= idx < len(weapons):
            if tokens[1] == "Left":
                if idx > 0:
                    weapon = weapons.pop(idx)
                    weapons.insert(idx - 1, weapon)
            elif tokens[1] == "Right":
                if idx < len(weapons):
                    weapon = weapons.pop(idx)
                    weapons.insert(idx + 1, weapon)
    elif tokens[0] == "Check":
        if tokens[1] == "Even":
            print(" ".join([x for i, x in enumerate(weapons) if i % 2 == 0]))
        elif tokens[1] == "Odd":
            print(" ".join([x for i, x in enumerate(weapons) if i % 2 == 1]))
    # "Move Left {index}":
    # "Move Right {index}":
    # "Check Even":
    # "Check Odd":



    command = input()


print("You crafted " + "".join(weapons) + "!")
