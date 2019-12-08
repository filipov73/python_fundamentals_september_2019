import re

number = int(input())

pattern = r"[U]\$(?P<user>[A-Z][a-z]{2,})[U]\$([P]\@\$)(?P<pass>[a-z]{5,}\d+)\2"
count = 0
for _ in range(number):
    line = input()

    match = re.match(pattern, line)
    if match:
        count += 1
        print(f"Registration was successful")
        print(f"Username: {match.group('user')}, Password: {match.group('pass')}")
    else:
        print(f"Invalid username or password")
print(f"Successful registrations: {count}")
