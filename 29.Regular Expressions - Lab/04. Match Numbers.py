import re

text = input()
pattern = r"(^|(?<=\s))(?P<target>[-]?[0-9]*[\.]?[0-9]*)($|(?=\s))"

match = re.finditer(pattern, text)

for m in match:
    print(m.group("target"), end=" ")
