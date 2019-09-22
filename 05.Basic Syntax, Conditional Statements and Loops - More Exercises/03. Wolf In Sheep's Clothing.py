array = input().split(", ")

if array[-1] == 'wolf':
    print(f"Please go away and stop eating my sheep")
else:
    wolf_index = array.index("wolf")
    new_array = array[wolf_index:]
    count_sheep = new_array.count("sheep")
    print(f"Oi! Sheep number {count_sheep}! You are about to be eaten by a wolf!")

