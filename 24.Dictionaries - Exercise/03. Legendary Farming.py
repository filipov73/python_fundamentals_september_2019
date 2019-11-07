def printing_items(items):
    for (k, v) in items.items():
        print(f"{k}: {v}")


data = input().split(" ")

items_dict = {
    'shards': 0,
    'motes': 0,
    'fragments': 0
}
end = False
while True:
    for idx in range(0, len(data), 2):
        key = data[idx+1].lower()
        value = int(data[idx])
        if key in items_dict:
            items_dict[key] += value
        else:
            items_dict[key] = value
        if items_dict['shards'] >= 250:
            items_dict['shards'] -= 250
            print("Shadowmourne obtained!")
            end = True
            break
        elif items_dict['motes'] >= 250:
            items_dict['motes'] -= 250
            print("Dragonwrath obtained!")
            end = True
            break
        elif items_dict['fragments'] >= 250:
            items_dict['fragments'] -= 250
            print("Valanyr obtained!")
            end = True
            break
    if end:break
    data = input().split(" ")

legendary_item = {key: value for (key, value) in items_dict.items() if key in ['shards', 'fragments', 'motes']}
junk_items = {key: value for (key, value) in items_dict.items() if key not in ['shards', 'fragments', 'motes']}

legendary_item_sorted = dict(sorted(legendary_item.items(), key=lambda x: (-x[1], x[0])))
junk_items_sorted = dict(sorted(junk_items.items(), key=lambda x: x[0]))

printing_items(legendary_item_sorted)
printing_items(junk_items_sorted)
