import re

pattern = r"^([#$%*&])(\w+)\1=(\d+)!!(.+)$"

while True:
    line = input()
    match = re.match(pattern, line)
    if match and int(match.group(3)) == len(match.group(4)):
        length = int(match.group(3))
        decrypt = [chr(ord(x)+length) for x in match.group(4)]
        print(f"Coordinates found! {match.group(2)} -> {''.join(decrypt)}")
        break
    else:
        print("Nothing found!")
