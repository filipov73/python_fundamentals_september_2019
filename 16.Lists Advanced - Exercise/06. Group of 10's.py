from math import ceil
num_list = list(map(int, input().split(", ")))

result_list = [[] for _ in range(ceil(int(max(num_list)) / 10))]

for n in num_list:
    idx = n // 10
    if n == 0:
        idx = 0
    elif n % 10 == 0:
        idx = n // 10 - 1

    result_list[idx].append(n)

for i in range(1, len(result_list) + 1):
    print(f"Group of {i*10}'s: {result_list[i-1]}")
