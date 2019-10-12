def odd_even_sum(st):
    odd_sum = 0
    even_sum = 0
    for ch in st:
        if int(ch) % 2 == 0:
            even_sum += int(ch)
        else:
            odd_sum += int(ch)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


str_num = input()
print(odd_even_sum(str_num))
