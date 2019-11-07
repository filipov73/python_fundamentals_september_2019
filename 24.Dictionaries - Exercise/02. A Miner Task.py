resource = input()

resources = {}

while resource != "stop":
    quantity = int(input())
    if resource in resources:
        resources[resource] += quantity
    else:
        resources[resource] = quantity
    resource = input()

for (resource, quantity) in resources.items():
    print(f"{resource} -> {quantity}")
