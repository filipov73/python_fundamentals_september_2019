string = input()

for i in range(len(string)):
    if string[i] == ":":
        print(string[i:i+2])
