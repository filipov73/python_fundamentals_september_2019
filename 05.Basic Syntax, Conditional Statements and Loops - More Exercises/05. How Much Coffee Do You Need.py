data = input()

coffees_cup = 0
target_list = ["coding", "dog", "cat", "movie"]
while data != "END":
    if data.lower() in target_list:
        if data.isupper():
            coffees_cup += 2
        elif data.islower():
            coffees_cup += 1
    data = input()
if coffees_cup > 5:
    print(f"You need extra sleep")
else:
    print(coffees_cup)
