stocks = input().split(" ")

bakery_dict = {}

for i in range(0, len(stocks) - 1, 2):
    bakery_dict[stocks[i]] = int(stocks[i+1])

print(bakery_dict)
