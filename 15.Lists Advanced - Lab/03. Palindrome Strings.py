string_list = input().split(" ")
search_word = input()

print([s for s in string_list if s == s[::-1]])
print(f"Found palindrome {string_list.count(search_word)} times")