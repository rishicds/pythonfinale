class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_percentage(self):
        return (self.marks / 100) * 100

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

class GraduateStudent(Student):
    def __init__(self, name, roll_no, marks, degree_program):
        super().__init__(name, roll_no, marks)
        self.degree_program = degree_program

    def assign_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

    def display(self):
        super().display()
        print(f"Degree Program: {self.degree_program}, Grade: {self.assign_grade()}")
