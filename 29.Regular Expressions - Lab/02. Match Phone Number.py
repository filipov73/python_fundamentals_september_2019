import re
text = input()

pattern = "\+359 2 [0-9]{3} [0-9]{4}|\+359-2-[0-9]{3}-[0-9]{4}\\b"
result = re.findall(pattern, text)
print(", ".join(result))
