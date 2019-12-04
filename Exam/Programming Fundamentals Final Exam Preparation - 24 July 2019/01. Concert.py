command = input()

concerts = {}

while command != "start of concert":
    tokens = command.split("; ")
    band_name = tokens[1]
    if tokens[0] == "Add":
        members = tokens[2].split(", ")
        if band_name not in concerts:
            concerts[band_name] = {"time": 0, "members": members}
        else:
            members_list = concerts[band_name]["members"]
            for member in members:
                if member not in members_list:
                    members_list.append(member)

    elif tokens[0] == "Play":
        time = int(tokens[2])
        if band_name not in concerts:
            concerts[band_name] = {"time": time, "members": []}
        else:
            concerts[band_name]["time"] += time

    command = input()

search_band = input()

total_time = sum([x[1]["time"] for x in concerts.items()])
sorted_bands = sorted(concerts.items(), key=lambda kvp: (-kvp[1]["time"], kvp[0]))
a = 5
print(f"Total time: {total_time}")
for item in sorted_bands:
    print(f"{item[0]} -> {item[1]['time']}")
filtered_search_band = [x for x in concerts.items() if x[0] == search_band][0]
print(f"{search_band}")
for member in filtered_search_band[1]["members"]:
    print(f"=> {member}")

