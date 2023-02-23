class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        if not isinstance(grades, list):
            raise TypeError("Grades have to be a list")
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

students_info = [
    {
        "name": "Santiago",
        "age": 20,
        "grades": [2.5, 3.5, 4.0, 0, 1.0]
    },
    {
        "name": "Sebastian",
        "age": 28,
        "grades": [3.9, 4.0, 4.0, 3.0, 4.2]
    },
    {
        "name": "neider",
        "age": 19,
        "grades": [4.5, 4.0, 4.9, 3.8, 4.2]
    }
]

students = [Student(student["name"], student["age"], student["grades"]) for student in students_info]

umbral = 3.8

best_students = [student for student in students if student.average_grade() >= umbral]

students_above_threshold = {student.name: student for student in students if student.average_grade() >= umbral}

print(f"Best students: {[student.name for student in best_students]}")

print(f"Students above {umbral}: {list(students_above_threshold.keys())}")

