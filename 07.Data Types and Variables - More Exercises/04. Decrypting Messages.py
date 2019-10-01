key = int(input())
n = int(input())

while n:
    character = input()
    print(chr(ord(character) + key), end='')
    n -= 1
