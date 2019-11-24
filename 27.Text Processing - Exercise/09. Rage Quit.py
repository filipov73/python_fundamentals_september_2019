text = input()

result = ""
digits = ""
res = ""
i = 0
while i < len(text):
    if not text[i].isdigit():
        res += text[i].upper()
        i += 1
    else:
        while text[i].isdigit():
            digits += text[i]
            i += 1
            if i >= len(text):
                break
        result += res * int(digits)
        res = ""
        digits = ""


length = len(set(result))
print(f"Unique symbols used: {length}")
print(result)
