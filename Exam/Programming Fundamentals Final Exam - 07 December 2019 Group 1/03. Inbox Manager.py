command = input()

information_dict = {}

while command != "Statistics":
    tokens = command.split("->")
    if tokens[0] == "Add":
        user = tokens[1]
        if user not in information_dict:
            information_dict[user] = []
        else:
            print(f"{user} is already registered")
    elif tokens[0] == "Send":
        user = tokens[1]
        email = tokens[2]
        # if user not in information_dict:
        #     information_dict[user] = [email]
        # else:
        information_dict[user].append(email)

    elif tokens[0] == "Delete":
        user = tokens[1]
        if user in information_dict:
            del information_dict[user]
        else:
            print(f"{user} not found!")

    command = input()

count = len(information_dict)
print(f"Users count: {count}")

sorted_information_dict = sorted(information_dict.items(), key=lambda x: (-len(x[1]), x[0]))

for item in sorted_information_dict:
    print(f"{item[0]}")
    for email in item[1]:
        print(f"- {email}")
