def is_palindrome(st):
    if st == st[::-1]:
        return True
    else:
        return False


string_num_list = input().split(", ")
for t in string_num_list:
    print(is_palindrome(t))
