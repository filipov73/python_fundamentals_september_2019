import re

total_sum = 0
print("Bought furniture:")
while True:
    text = input()
    if text == "Purchase":
        print(f"Total money spend: {total_sum:.2f}")
        break
    pattern = r">>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)"
    match = re.findall(pattern, text)
    for m in match:
        print(m[0])
        total_sum += float(m[1]) * int(m[2])
