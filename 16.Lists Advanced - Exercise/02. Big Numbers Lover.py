numbers = input().split(" ")

numbers.sort(reverse=True)
print("".join(map(str, numbers)))
