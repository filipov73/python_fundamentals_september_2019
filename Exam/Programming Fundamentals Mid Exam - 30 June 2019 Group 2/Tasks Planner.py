times = [int(x) for x in input().split(" ")]
command = input()

while command != "End":
    tokens = command.split(" ")
    if tokens[0] == "Complete":
        idx = int(tokens[1])
        if 0 <= idx < len(times):
            times[idx] = 0
    elif tokens[0] == "Change":
        idx = int(tokens[1])
        time = int(tokens[2])
        if 0 <= idx < len(times):
            times[idx] = time
    elif tokens[0] == "Drop":
        idx = int(tokens[1])
        if 0 <= idx < len(times):
            times[idx] = -1
    elif tokens[0] == "Count":
        if tokens[1] == "Completed":
            print(len([x for x in times if x == 0]))
        elif tokens[1] == "Incomplete":
            print(len([x for x in times if x > 0]))
        elif tokens[1] == "Dropped":
            print(len([x for x in times if x < 0]))

    command = input()

result = [str(x) for x in times if x > 0]
print(" ".join(result))
