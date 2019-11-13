string = input()
digits = ""
letters = ""
other = ""

for ch in string:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    elif not ch.isalnum():
        other += ch
print(digits)
print(letters)
print(other)
