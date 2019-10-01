party = int(input())
days = int(input())

companions_count = party
coins = 0

for day in range(1, days + 1):
    if day % 10 == 0:
        companions_count -= 2
    if day % 15 == 0:
        companions_count += 5
    coins += 50 - (companions_count * 2)
    if day % 3 == 0:
        coins -= (companions_count * 3)
    if day % 5 == 0:
        coins += (companions_count * 20)
        if day % 3 == 0:
            coins -= (companions_count * 2)

print(f"{companions_count} companions received {int(coins / companions_count)} coins each.")
