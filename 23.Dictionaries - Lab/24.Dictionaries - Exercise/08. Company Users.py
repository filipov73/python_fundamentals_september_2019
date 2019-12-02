command = input().split(" -> ")

companies_employees_dict = {}

while command[0] != "End":
    company_name = command[0]
    employee_id = command[1]
    if company_name not in companies_employees_dict:
        companies_employees_dict[company_name] = [employee_id]
    else:
        if employee_id not in companies_employees_dict[company_name]:
            companies_employees_dict[company_name].append(employee_id)

    command = input().split(" -> ")

for (key, value) in sorted(companies_employees_dict.items()):
    print(f"{key}")
    for id_ in value:
        print(f"-- {id_}")
