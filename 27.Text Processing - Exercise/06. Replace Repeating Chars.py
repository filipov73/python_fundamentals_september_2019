string = input() + " "


for i in range(1, len(string)):
    if string[i-1] != string[i]:
        print(string[i-1], end="")

