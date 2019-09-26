number = int(input())
sum_character = 0

while number:
    st = input()
    sum_character += ord(st)
    number -= 1
print(f'The sum equals: {sum_character}')
