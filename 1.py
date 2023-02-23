class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        if not isinstance(grades, list):
            raise TypeError("grades debe ser una lista")
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student_dic = {
    "name": "Santiago",
    "age": 20,
    "grades": [2.5, 3.5, 4.0, 0, 1.0]
}

students = [Student(d["name"], d["age"], d["grades"]) for d in [student_dic]]

Student.add_grade(3.0)
average = Student.average_grade()
print(f"the average of the  {Student.name} is {average}")






