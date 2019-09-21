quantity = int(input())
days = int(input())

price_ornament_set = 2.00
price_tree_skirt = 5.00
price_tree_garlands = 3.00
price_tree_lights = 15.00


counter_days = 1
total_cost = 0
total_spirit = 0

while days >= counter_days:
    if counter_days % 2 == 0:
        total_cost += price_ornament_set * quantity
        total_spirit += 5
    if counter_days % 3 == 0:
        total_cost += (price_tree_skirt * quantity) + (price_tree_garlands * quantity)
        total_spirit += 13
    if counter_days % 5 == 0:
        total_cost += (price_tree_lights * quantity)
        total_spirit += 17
        if counter_days % 3 == 0:
            total_spirit += 30
    if counter_days % 10 == 0:
        total_cost += 2 * (price_tree_skirt * quantity) + (price_tree_garlands * quantity) + (price_tree_lights * quantity)
        total_spirit -= 20
        # quantity += 2
    if (counter_days == days) and counter_days % 10 == 0:
        total_spirit -= 30
    counter_days += 1


print(f"Total cost: {int(total_cost)}")
print(f"Total spirit: {total_spirit}")
