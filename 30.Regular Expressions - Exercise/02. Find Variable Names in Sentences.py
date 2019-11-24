import re

text = input()
pattern = r"(?<=[^_]_)([a-zA-Z0-9]+)(?=\b)"

match = re.finditer(pattern, text)



print(",".join(m.group(1) for m in match))


