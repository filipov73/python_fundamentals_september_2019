arsenal_cards = input().split(":")
command = input()
new_cards = []
while command != "Ready":
    tokens = command.split(" ")
    if tokens[0] == "Add":
        name = tokens[1]
        if name in arsenal_cards:
            new_cards.append(name)
        else:
            print("Card not found.")
    elif tokens[0] == "Insert":
        name = tokens[1]
        idx = int(tokens[2])
        if (0 <= idx < len(new_cards)) and (name in arsenal_cards):
            new_cards.insert(idx, name)
        else:
            print("Error!")
    elif tokens[0] == "Remove":
        name = tokens[1]
        if name in new_cards:
            new_cards.remove(name)
        else:
            print("Card not found.")
    elif tokens[0] == "Swap":
        name_1 = tokens[1]
        name_2 = tokens[2]
        # temp = new_cards[new_cards.index(name_1)]
        # new_cards[new_cards.index(name_1)] = name_2
        # new_cards[new_cards.index(name_2, 1)] = temp
        new_cards[new_cards.index(name_1)], new_cards[new_cards.index(name_2, 1)] = name_2 , name_1

    elif tokens[0] == "Shuffle" and tokens[1] == "deck":
        new_cards.reverse()

    command = input()


print(" ".join(new_cards))
