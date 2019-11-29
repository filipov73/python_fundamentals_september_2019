import re
number = int(input())


for _ in range(number):
    text = input()
    pattern = r"^(?P<tag>[${1}|%{1}])([A-Z][a-z]{2,})(?P=tag)[:][ ]\[(\w+)\]\|\[(\w+)\]\|\[(\w+)\]\|$"
    matches = re.match(pattern, text)
    if matches:
        tag = matches.group(2)
        num_1 = int(matches.group(3))
        num_2 = int(matches.group(4))
        num_3 = int(matches.group(5))
        print(f"{tag}: {chr(num_1)}{chr(num_2)}{chr(num_3)}")
    else:
        print(f"Valid message not found!")
