import re
text = input()

pattern = ""
result = re.findall(pattern, text)
print(", ".join(result))
