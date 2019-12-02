name = input()

products_price_dict = {}

while name != "buy":
    product, price, quantity = name.split(" ")
    if product in products_price_dict:
        products_price_dict[product][0] = float(price)
        products_price_dict[product][1] += int(quantity)
    else:
        products_price_dict[product] = [float(price), float(quantity)]

    name = input()

for key, value in products_price_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
