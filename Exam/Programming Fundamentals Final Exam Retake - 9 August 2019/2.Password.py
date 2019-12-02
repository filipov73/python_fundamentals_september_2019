import re
number = int(input())

pattern = r"^(?P<start>.+)\>(?P<first>\d{3})[|](?P<second>[a-z]{3})[|](?P<third>[A-Z]{3})[|](?P<fourth>[^>|<]{3})\<(?P<end>.+)$"

for _ in range(number):
    password = input()
    target = re.match(pattern, password)
    if target:
        if target.group("start") == target.group("end"):
            res = target.group("first") + target.group("second") + target.group("third") + target.group("fourth")
            print(f"Password: {res}")
    else:
        print(f"Try another password!")

