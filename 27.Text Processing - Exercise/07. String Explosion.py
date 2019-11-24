string = input()
new_string = ""
i = 0
add_explosion = 0
while string:
    if string[i] == ">":
        new_string += string[:i+1]
        explosion = int(string[i+1])
        remove_chars = string[i+1:i+explosion+add_explosion+1]

        if ">" in remove_chars:
            find_idx = string.find(">", 1)
            string = string[find_idx:]
            add_explosion = explosion - (find_idx - 1)
        else:
            string = string[i+explosion+add_explosion+1:]
            add_explosion = 0
    else:
        new_string += string[i]
        string = string[i+1:]
print(new_string)

