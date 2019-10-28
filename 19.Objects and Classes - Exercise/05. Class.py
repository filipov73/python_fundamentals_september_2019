class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []
        self.average_grade = 0

    def add_student(self, name, grade):
        if Class.__students_count > 0:
            Class.__students_count -= 1
            self.students.append(name)
            self.grades.append(float(grade))

    def get_average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        return 0

    def __repr__(self):
        return f"The students in {self.name}: " \
               + ", ".join(self.students) \
               + f". Average grade: {self.get_average_grade():.2f}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
