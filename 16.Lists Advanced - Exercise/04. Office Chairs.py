num_rooms = int(input())

free_chairs = 0
no_chairs = True

for r in range(1, num_rooms + 1):
    data = input().split(" ")
    chairs = len(data[0])
    peoples = int(data[1])
    if chairs < peoples:
        print(f"{peoples - chairs} more chairs needed in room {r}")
        no_chairs = False
    else:
        free_chairs += chairs - peoples
if no_chairs:
    print(f"Game On, {free_chairs} free chairs left")
