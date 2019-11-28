import re
text = input().lower()
search = input().lower()

# pattern = f"\\b{search}\\b"
pattern = rf"\b{search}\b"
match = re.findall(pattern, text)
# matches = re.findall(pattern, text, flags=re.IGNORECASE)

print(len(match))
