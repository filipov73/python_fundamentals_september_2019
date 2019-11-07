
stock = {}

command = input()
while command != "statistics":
    product, quantity = command.split(": ")
    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)
    command = input()

print("Products in stock:")
for item in stock.items():
    print(f"- {item[0]}: {item[1]}")

total_quantity = sum([x for x in stock.values()])
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {total_quantity}")
