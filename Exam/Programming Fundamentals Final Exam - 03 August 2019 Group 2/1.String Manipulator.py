string = input()
command = input()

while command != "Done":
    tokens = command.split(" ")
    if tokens[0] == "Change":
        _, char, replacement = tokens
        string = string.replace(char, replacement)
        print(string)
    elif tokens[0] == "Includes":
        _, check_str = tokens
        if check_str in string:
            print(True)
        else:
            print(False)
    elif tokens[0] == "End":
        _, end = tokens
        if string.endswith(end):
            print(True)
        else:
            print(False)
    elif tokens[0] == "Uppercase":
        string = string.upper()
        print(string)
    elif tokens[0] == "FindIndex":
        _, find_char = tokens
        idx = string.index(find_char)
        print(idx)
    elif tokens[0] == "Cut":
        start_index = int(tokens[1])
        length = int(tokens[2])
        end_index = start_index + length
        cut = string[start_index:end_index]
        print(cut)
    command = input()

