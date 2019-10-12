def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


string_list = input().split(", ")
for t in string_list:
    print(palindrome(t))

