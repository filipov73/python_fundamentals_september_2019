import re

pattern = r"^(?P<artist>[A-Z'][a-z' ]+):(?P<song>([A-Z ]+)+)$"

command = input()

while command != "end":
    match = re.match(pattern, command)
    if match:
        artist = match.group("artist")
        song = match.group("song")
        length = len(artist)
        encrypted_artist = ""
        encrypted_song = ""
        for ch in artist:
            if length + ord(ch) > 122:
                orf_num = length + ord(ch) - 122 + 97 - 1
                ch = chr(orf_num)
            elif length + ord(ch) > 90 and length + ord(ch) < 96:
                orf_num = length + ord(ch) - 90 + 65 - 1
                ch = chr(orf_num)
            elif ch == ":":
                ch = "@"
            elif ch == " ":
                ch == " "
            elif ch == "'":
                ch = "'"
            else:
                ch = chr(ord(ch) + length)
            encrypted_artist += ch
        for ch in song:
            if length + ord(ch) > 122:
                orf_num = length + ord(ch) - 122 + 97 - 1
                ch = chr(orf_num)
            elif length + ord(ch) > 90:# and length + ord(ch) < 96:
                orf_num = length + ord(ch) - 90 + 65 - 1
                ch = chr(orf_num)
            elif ch == ":":
                ch = "@"
            elif ch == " ":
                ch == " "
            elif ch == "'":
                ch = "'"
            else:
                ch = chr(ord(ch) + length)
            encrypted_song += ch

        print(f"Successful encryption: {encrypted_artist}@{encrypted_song}")
    else:
        print("Invalid input!")
    command = input()
