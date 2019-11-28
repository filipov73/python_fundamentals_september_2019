import re
text = input()

pattern = r'\b[a-z][\w\.\-\_]*@[a-z][a-z\.\-\_]*\b\w+'
# r"(?<=\s)[a-z0-9]+[a-z0-9.-]+@[a-z0-9.-]*[.]\b\w+"

match = re.findall(pattern, text)

for m in match:
    print(m)
