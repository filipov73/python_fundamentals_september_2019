import re

pattern = r"([*|@])(?P<tag>[A-Z][]a-z]{2,})\1:[ ]\[([A-Za-z]+)\]\|\[([A-Za-z]+)\]\|\[([A-Za-z]+)\]\|$"

number = int(input())

for _ in range(number):
    line = input()
    matches = re.search(pattern, line)
    if matches:
        print(f"{matches.group('tag')}: {ord(matches.group(3))} {ord(matches.group(4))} {ord(matches.group(5))}")
    else:
        print("Valid message not found!")

