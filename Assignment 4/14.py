class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}
    def add_mark(self, subject, score):
        if score < 0 or score > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return
        self.marks[subject] = score
    def calculate_average(self):
        if len(self.marks) == 0:
            return None
        total = 0
        for score in self.marks.values():
            total += score
        return total / len(self.marks)
    def get_grade(self):
        average = self.calculate_average()
        if average is None:
            return "N/A"
        elif average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"
student = Student("Biki", 101)
student.add_mark("Python", 85)
student.add_mark("Math", 92)
student.add_mark("Physics", 78)
print("Student Name:", student.name) # Biki
print("Roll Number:", student.roll_number) # 101
print("Marks:", student.marks) # {'Python': 85, 'Math': 92, 'Physics': 78}
print("Average:", student.calculate_average()) # 85.0
print("Grade:", student.get_grade()) # A