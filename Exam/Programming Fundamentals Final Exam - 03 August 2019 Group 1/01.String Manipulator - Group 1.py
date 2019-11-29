import re
string = input()

command = input()

while command != "End":
    token = command.split(" ")
    if len(token) == 3:
        if token[0] == "Translate":
            char, replacement = token[1:]
            string = string.replace(char, replacement)
            print(string)
        elif token[0] == "Remove":
            idx = int(token[1])
            count = int(token[2])
            remove_str = string[idx:count]
            string = string.replace(remove_str, "")
            print(string)
            pass
    elif len(token) == 2:
        if token[0] == "Includes":
            search_str = token[1]
            if search_str in string:
                print(True)
            else:
                print(False)
        elif token[0] == "Start":
            start_str = token[1]
            matches = re.findall(rf"^{start_str}", string)
            if matches:
                print(True)
            else:
                print(False)
        elif token[0] == "FindIndex":
            res = string[::-1]
            last_rev = res.index(token[1])
            print(len(res) - last_rev - 1)
    elif len(token) == 1:
    # else:
        if token[0] == "Lowercase":
            string = string.lower()
            print(string)

    command = input()
