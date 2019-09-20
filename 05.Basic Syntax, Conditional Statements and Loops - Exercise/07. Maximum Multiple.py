divisor = int(input())
bound = int(input())

for n in range(1, bound + 1):
    if n % divisor == 0:
        max_num = n

print(max_num)
