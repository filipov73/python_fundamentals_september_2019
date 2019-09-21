quantity = int(input())
days = int(input())

price_ornament_set = 2
price_tree_skirt = 5
price_tree_garlands = 3
price_tree_lights = 15
day = 1
total_cost = 0
total_spirit = 0

while day <= days:
    if day % 2 == 0:
        total_cost += price_ornament_set * quantity
        total_spirit += 5
    if day % 3 == 0:
        total_cost += ((price_tree_skirt * quantity) + (price_tree_garlands * quantity))
        total_spirit += 13
    if day % 5 == 0:
        total_cost += (price_tree_lights * quantity)
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_cost += price_tree_skirt  + price_tree_garlands + price_tree_lights
        total_spirit -= 20

    if (day == days) and day % 10 == 0:
        total_spirit -= 30
    day += 1
    if day % 11 == 0:
        quantity += 2


print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
