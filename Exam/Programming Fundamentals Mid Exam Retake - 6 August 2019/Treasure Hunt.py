treasure_chest_list = input().split('|')
command = input()

while command != "Yohoho!":
    command = command.split(" ")
    if command[0] == "Loot":
        for d in command[1:]:
            if d not in treasure_chest_list:
                treasure_chest_list.insert(0, d)
    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(treasure_chest_list):
            item = treasure_chest_list.pop(int(command[1]))
            treasure_chest_list.append(item)
    elif command[0] == "Steal":
        count = int(command[1])
        if count > len(treasure_chest_list):
            count = len(treasure_chest_list)
        steal_list = treasure_chest_list[-count:]
        treasure_chest_list = treasure_chest_list[:-count]
        print(", ".join(steal_list))
    command = input()


if len(treasure_chest_list) == 0:
    print("Failed treasure hunt.")
else:
    # sum_letter = 0
    # for item in new_treasure_chest_list:
    #     sum_letter += len(str(item))
    average = sum([len(x) for x in treasure_chest_list]) / len(treasure_chest_list)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
