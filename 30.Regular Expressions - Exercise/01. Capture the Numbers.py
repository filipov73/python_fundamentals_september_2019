import re

text = input()
st = ""
while text:
    st += text + " "
    text = input()

pattern = r"\d+"

match = re.findall(pattern, st)

for m in match:
    print(m, end=" ")
