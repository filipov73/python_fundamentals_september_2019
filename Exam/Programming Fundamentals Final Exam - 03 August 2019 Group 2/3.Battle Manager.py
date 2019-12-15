command = input()

information_dict = {}

while command != "Results":
    tokens = command.split(":")
    if tokens[0] == "Add":
        name = tokens[1]
        health = int(tokens[2])
        energy = int(tokens[3])
        if name not in information_dict:
            information_dict[name] = {"health": health, "energy": energy}
        else:
            information_dict[name]["health"] += health
    elif tokens[0] == "Attack":
        attacker = tokens[1]
        defender = tokens[2]
        damage = int(tokens[3])
        if attacker in information_dict and defender in information_dict:
            information_dict[defender]["health"] -= damage
            information_dict[attacker]["energy"] -= 1
            if information_dict[defender]["health"] <= 0:
                print(f"{defender} was disqualified!")
                del information_dict[defender]
            if information_dict[attacker]["energy"] <= 0:
                print(f"{attacker} was disqualified!")
                del information_dict[attacker]
    elif tokens[0] == "Delete":
        name = tokens[1]
        if name == "All":
            information_dict = {}
        elif name in information_dict:
            del information_dict[name]
    command = input()

count = len(information_dict)
sorted_information_dict = sorted(information_dict.items(), key=lambda x: (-x[1]["health"], x[0]))
print(f"People count: {count}")
for item in sorted_information_dict:
    person = item[0]
    health = item[1]["health"]
    energy = item[1]["energy"]
    print(f"{person} - {health} - {energy}")
