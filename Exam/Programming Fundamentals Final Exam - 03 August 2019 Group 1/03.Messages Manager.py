capacity  = int(input())

messages = {}

command = input()

while True:
    if command == "Statistics":
        break
    token = command.split("=")
    if len(token) == 4:
        _, username, sent, received = token
        if username not in messages:
            messages[username] = {"sent": int(sent), "received": int(received)}
    elif len(token) == 3:
        _, sender, receiver = token
        if (sender and receiver) in messages:
            messages[sender]["sent"] += 1
            messages[receiver]["received"] += 1
            if (messages[sender]["sent"] + messages[sender]["received"]) == capacity:
                print(f"{sender} reached the capacity!")
                del messages[sender]
            elif (messages[receiver]["sent"] + messages[receiver]["received"]) == capacity:
                print(f"{receiver} reached the capacity!")
                del messages[receiver]
    elif len(token) == 2:
        _, username = token
        if username in messages:
            del messages[username]
        elif username == "All":
            messages = {}

    command = input()

sorted_messages = dict(sorted(messages.items(), key=lambda kvp: (-kvp[1]["received"], kvp[0])))

print(f"Users count: {len(messages)}")

for item in sorted_messages.items():
    print(f"{item[0]} - {item[1]['sent'] + item[1]['received']}")
