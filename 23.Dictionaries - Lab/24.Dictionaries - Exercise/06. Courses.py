command = input().split(" : ")

courses_dict = {}

while command[0] != "end":
    course_name = command[0]
    student_name = command[1]
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)
    command = input().split(" : ")

courses_dict_sorted = sorted(courses_dict.items(), key=lambda x: -len(x[1]))

for cource, names in courses_dict_sorted:
    print(f"{cource}: {len(names)}")
    for name in sorted(names):
        print(f"-- {name}")
