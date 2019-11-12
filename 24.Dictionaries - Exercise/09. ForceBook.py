command = input()

force_book = {}

while command != "Lumpawaroo":
    if " | " in command:
        side, user = command.split(" | ")
        if side not in force_book:
            force_book[side] = []
        if user not in force_book[side]:
            force_book[side].append(user)
    elif " -> " in command:
        user, side = command.split(" -> ")
        if side not in force_book:
            force_book[side] = []
        # if user not in list(x for y in force_book.values() for x in y):
        if user not in force_book[side]:
            force_book[side].append(user)
            print(f"{user} joins the {side} side!" )
        else:
            remove_user_side = [x for x in force_book.keys() if x != side][0]
            change_user_side = force_book[remove_user_side].pop(force_book[remove_user_side].index(user))
            force_book[side].append(user)
            print(f"{user} joins the {side} side!" )

    command = input()

force_book_sorted = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))

for (key, value) in force_book_sorted.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        value_sorted = sorted(value)
        for v in value_sorted:
            print(f"! {v}")

