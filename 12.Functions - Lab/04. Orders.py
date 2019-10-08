def order(product, quantity):
    price = None
    if product == "coffee":
        price = quantity * 1.50
    elif product == "water":
        price = quantity * 1.00
    elif product == "coke":
        price = quantity * 1.40
    elif product == "snacks":
        price = quantity * 2.00
    return f"{price:.2f}"


product = input()
quantity = int(input())

print(order(product, quantity))
