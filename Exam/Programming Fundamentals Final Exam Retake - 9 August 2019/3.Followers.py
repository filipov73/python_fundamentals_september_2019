command = input()

information_dict = {}
username_list = []

while command != "Log out":
    token = command.split(": ")
    if token[0] == "New follower":
        username = token[1]
        if username not in username_list:
            information_dict[username] = {"likes": 0, "comments": 0}
            username_list.append(username)
    elif token[0] == "Like":
        username = token[1]
        count = int(token[2])
        if username not in username_list:
            information_dict[username] = {"likes": count, "comments": 0}
            username_list.append(username)
        else:
            information_dict[username]["likes"] += count
    elif token[0] == "Comment":
        username = token[1]
        if username not in username_list:
            information_dict[username] = {"likes": 0, "comments": 1}
            username_list.append(username)
        else:
            information_dict[username]["comments"] += 1
    elif token[0] == "Blocked":
        username = token[1]
        if username not in username_list:
            print(f"{username} doesn't exist.")
        else:
            del information_dict[username]
            username_list.remove(username)

    command = input()

sorted_info_dict = dict(sorted(information_dict.items(), key=lambda kvp: (-kvp[1]["likes"], kvp)))
print(f"{len(information_dict)} followers")
for name, likes_comments in sorted_info_dict.items():
    user = name
    sums = likes_comments["likes"] + likes_comments["comments"]
    print(f"{user}: {sums}")
