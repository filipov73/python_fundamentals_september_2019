rows = int(input())
capacity = 255
sum_liters = 0
for line in range(1, rows + 1):
    liters = int(input())
    sum_liters += liters
    if capacity < sum_liters:
        print(f'Insufficient capacity!')
        sum_liters -= liters
print(sum_liters)
