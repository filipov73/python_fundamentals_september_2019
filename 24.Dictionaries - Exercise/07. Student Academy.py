number = int(input())

students_grades = {}

for _ in range(number):
    name = input()
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = [grade]
    else:
        students_grades[name].append(grade)

students_grades_higher_450 = {key: sum(value) / len(value) for (key, value) in students_grades.items() if sum(value) / len(value) >= 4.50}

average_grade_sorted = sorted(students_grades_higher_450.items(), key=lambda g: -g[1])

for students_average_grade in average_grade_sorted:
    print(f"{students_average_grade[0]} -> {students_average_grade[1]:.2f}")
