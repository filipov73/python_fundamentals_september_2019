string = input()

command = input()

while command != "Complete":
    tokens = command.split(" ")

    if tokens[0] == "Make":
        if tokens[1] == "Upper":
            string = string.upper()
            print(string)
        elif tokens[1] == "Lower":
            string = string.lower()
            print(string)
    elif tokens[0] == "GetDomain":
        count = int(tokens[1])
        res = string[-3:len(string)]
        print(res)
    elif tokens[0] == "GetUsername":
        search = string.find("@")
        if search >= 0:
            print(string[:7])
        else:
            print(f"The email {string} doesn't contain the @ symbol.")
    elif tokens[0] == "Replace":
        rep = tokens[1]
        string = string.replace(rep, "-")
        print(string)
    elif tokens[0] == "Encrypt":
        for ch in string:
            print(ord(ch), end=" ")

    command = input()


