register = {}

while True:
    command = input().split(" -> ")
    company_name = command[0]
    if company_name == "End":
        break
    employee_id = command[1]

    if company_name not in register:
        register[company_name] = []
    # register[company_name].append(employee_id)

    if employee_id not in register[company_name]:
        register[company_name].append(employee_id)

sorted_dict = sorted(register)


for (key, value) in sorted(register.items()):
    print(f"{key}")
    for id_ in value:
        print(f"-- {id_}")