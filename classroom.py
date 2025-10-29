class Classroom:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def class_average(self):
        total_marks = sum(student.get_marks() for student in self.students)
        return total_marks / len(self.students)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda student: student.get_marks())

    def show_all_students(self):
        for student in self.students:
            print(student)