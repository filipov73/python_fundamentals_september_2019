import re
number = int(input())

# pattern = r"^(?P<start>.+)\>(?P<first>\d{3})[|](?P<second>[a-z]{3})[|](?P<third>[A-Z]{3})[|](?P<fourth>[^>|<]{3})\<(?P<end>.+)$"
pattern = r"^(?P<start>.+)\>(?P<first>\d{3})[|](?P<second>[a-z]{3})[|](?P<third>[A-Z]{3})[|](?P<fourth>[^>|<]{3})\<(?P=start)$"

for _ in range(number):
    password = input()
    target = re.match(pattern, password)
    if target:
        res = target.group("first") + target.group("second") + target.group("third") + target.group("fourth")
        print(f"Password: {res}")
    else:
        print(f"Try another password!")

