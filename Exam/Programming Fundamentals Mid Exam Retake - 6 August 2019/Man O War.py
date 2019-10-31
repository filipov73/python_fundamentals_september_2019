pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())

command = input()

while command != "Retire":
    tokens = command.split(" ")
    if tokens[0] == "Fire":
        idx = tokens[1]
        damage = tokens[2]
        if 0 <= idx < len(warship):
            warship[idx] -= damage
            if warship[idx] <= 0:
                print("You won! The enemy ship has sunken.")
                break
    elif tokens[0] == "Defend":
        start_idx = tokens[1]
        end_idx = tokens[2]
        damage = tokens[3]
        print("You lost! The pirate ship has sunken.")
    elif tokens[0] == "Repair":
        pass
    elif tokens[0] == "Status":
        pass
    # Fire {index} {damage}
    # Defend {startIndex} {endIndex}{damage}
    # Repair {index} {health}
    # Status
    command = input()
