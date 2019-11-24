import re

text = input()

pattern = r"(?P<day>[0-9][0-9])(?P<sep>[\.\-/])(?P<month>[A-Z][a-z]{2})(?P=sep)(?P<year>[0-9]{4})"
match = re.finditer(pattern, text)

for m in match:
    print(f"Day: {m.group('day')}, Month: {m.group('month')}, Year: {m.group('year')}")
