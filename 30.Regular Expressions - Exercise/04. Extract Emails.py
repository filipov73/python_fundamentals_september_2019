import re
text = input()

pattern = r'\b[a-z][\w\.\-\_]*@[a-z][a-z\.\-\_]*\b\w+'

match = re.findall(pattern, text)

for m in match:
    print(m)
