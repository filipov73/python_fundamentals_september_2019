num = int(input())

target_sum_num = [5, 7, 11]

for n in range(1, num + 1):
    sum_digit = sum(list(map(int, str(n))))
    if sum_digit in target_sum_num:
        special_num = True
    else:
        special_num = False
    print(f'{n} -> {special_num}')
