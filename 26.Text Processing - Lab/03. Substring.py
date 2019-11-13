search_word = input()
string = input()

while search_word in string:
    string = string.replace(search_word, "")

print(string)
