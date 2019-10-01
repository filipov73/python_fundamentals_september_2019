lines = int(input())

bracket_list = []
balanced = None

while lines:
    text = input()
    if len(text) == 1 and (ord(text) == 40 or ord(text) == 41):
        bracket_list.append(ord(text))
    lines -= 1
for i in range(0, len(bracket_list), 2):
    if bracket_list[i] == 40 and bracket_list[i+1] == 41:
        balanced = "BALANCED"
    else:
        balanced = "UNBALANCED"
print(balanced)
