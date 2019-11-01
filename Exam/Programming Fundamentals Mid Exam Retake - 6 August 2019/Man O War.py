pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())

stalemate = True
command = input()

while command != "Retire":
    tokens = command.split(" ")
    if tokens[0] == "Fire":
        idx = int(tokens[1])
        damage = int(tokens[2])
        if 0 <= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break
    elif tokens[0] == "Defend":
        start_idx = int(tokens[1])
        end_idx = int(tokens[2])
        damage = int(tokens[3])
        if start_idx >= 0 and end_idx < len(pirate):
            for i in range(start_idx, end_idx + 1):
                pirate[i] -= damage
                # if pirate[i] <= 0:
                #     pass
            if not all([False for x in pirate[start_idx:end_idx + 1] if x <= 0]):
                print("You lost! The pirate ship has sunken.")
                stalemate = False
                break
    elif tokens[0] == "Repair":
        idx = int(tokens[1])
        health = int(tokens[2])
        if 0 <= idx < len(pirate):
            pirate[idx] += health
            if pirate[idx] > max_health:
                pirate[idx] = max_health
    elif tokens[0] == "Status":
        lower_than_20 = max_health * 0.20
        count = len([x for x in pirate if x < lower_than_20])
        print(f"{count} sections need repair.")
    # Fire {index} {damage}
    # Defend {startIndex} {endIndex}{damage}
    # Repair {index} {health}
    # Status
    command = input()

if stalemate:
    print(f"Pirate ship status: {sum(pirate)}")
    print(f"Warship status: {sum(warship)}")
