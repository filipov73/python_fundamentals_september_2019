tickets = input().split(", ")

for ticket in tickets:
    if len(tickets) == 20:
        if ('@'or '#' or '$'or '^') not in ticket:
            print(f'ticket "{ticket}" - no match')
        else:
            left_half = ticket[:10]
            right_half = ticket[10:]
    else:
        print("invalid ticket")





# :
# •	Invalid ticket - "invalid ticket"
# •	No match - "ticket "{ticket}" - no match"
# •	Match with length 6 to 9 - "ticket "{ticket}" - {match length}{match symbol}"
# •	Match with length 10 - "ticket "{ticket}" - {match length}{match symbol} Jackpot!"
