
def validator(password):
    len_digits = 0
    valid = True
    if not(6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        valid = False
    for ch in password:
        ch_asccii = ord(ch)
        if not (48 <= ch_asccii <= 57 or 65 <= ch_asccii <= 90 or 97 <= ch_asccii <= 122):
            print("Password must consist only of letters and digits")
            valid = False
            break
    for ch in password:
        if ch.isdigit():
            len_digits += 1
    if len_digits < 2:
        print("Password must have at least 2 digits")
        valid = False
    if valid:
        print("Password is valid")


password = input()
validator(password)
