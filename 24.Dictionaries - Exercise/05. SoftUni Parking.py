number = int(input())
parking_place_dict = {}

username = None
license_plate_number = None

for _ in range(number):
    data = input().split(" ")
    if data[0] == "register":
        username = data[1]
        license_plate_number = data[2]
        if username not in parking_place_dict:
            parking_place_dict[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif data[0] == "unregister":
        username = data[1]
        if username not in parking_place_dict:
            print(f"ERROR: user {username} not found")
        else:
            parking_place_dict.pop(username)
            print(f"{username} unregistered successfully")


for (key, value) in parking_place_dict.items():
    print(f"{key} => {value}")
