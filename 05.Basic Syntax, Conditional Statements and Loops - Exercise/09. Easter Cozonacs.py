budget = float(input())
price_flour = float(input())

price_eggs_pack = price_flour * 0.75
price_milk_liter = price_flour * (1 + 0.25)
price_cozonac = price_flour + price_eggs_pack + (price_milk_liter / 4)
colored_eggs = 0
count_cozonacs = 0

while budget > price_cozonac:
    budget -= price_cozonac
    count_cozonacs += 1
    colored_eggs += 3
    if count_cozonacs % 3 == 0:
        colored_eggs -= count_cozonacs - 2



print(f"You made {count_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
