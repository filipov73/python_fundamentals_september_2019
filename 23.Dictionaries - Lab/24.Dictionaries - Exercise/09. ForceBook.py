command = input()

force_book = {}

while command != "Lumpawaroo":
    if " | " in command:
        side, user = command.split(" | ")
        if side not in force_book:
            force_book[side] = []
        a = list(x for y in force_book.values() for x in y)
        if user not in a:
            force_book[side].append(user)
    elif " -> " in command:
        user, side = command.split(" -> ")
        if side not in force_book:
            force_book[side] = []
        a = list(x for y in force_book.values() for x in y)
        if user not in a:
            force_book[side].append(user)
            print(f"{user} joins the {side} side!")
        else:
            for (key, value) in force_book.items():
                if user in value:
                    force_book[key].remove(user)

            force_book[side].append(user)
            # remove_user_side = [key for (key, value) in force_book.items() if user in value][0]
            # change_user_side = force_book[remove_user_side].pop(force_book[remove_user_side].index(user))
            # force_book[side].append(user)
            print(f"{user} joins the {side} side!")

    command = input()

force_book_sorted = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))

for (key, value) in force_book_sorted.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        value_sorted = sorted(value)
        for v in value_sorted:
            print(f"! {v}")

