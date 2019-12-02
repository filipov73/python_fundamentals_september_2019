string = input()

command = input()

while command != "Sign up":
    token = command.split(" ")
    if token[0] == "Case":
        if token[1] == "lower":
            string = string.lower()
            print(string)
        elif token[1] == "upper":
            string = string.upper()
            print(string)
    elif token[0] == "Reverse":
        start_index = int(token[1])
        end_index = int(token[2])
        if start_index >= 0 and end_index < len(string):
            res = string[start_index:end_index + 1]
            print(res[::-1])
    elif token[0] == "Cut":
        substring = token[1]
        if substring in string:
            string = string.replace(substring, "")
            print(string)
        else:
            print(f"The word {string} doesn't contain {substring}.")
    elif token[0] == "Replace":
        char = token[1]
        string = string.replace(char, "*")
        print(string)
    elif token[0] == "Check":
        char = token[1]
        if char in string:
            print(f"Valid")
        else:
            print(f"Your username must contain {char}.")

    command = input()

