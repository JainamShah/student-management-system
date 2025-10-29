# class Student:
#     def __init__(self, name, age, grade):
#         self.__name = name          # Private attribute
#         self.__age = age            # Private attribute
#         self.grade = grade        # Private attribute
    
#     def get_age(self):          # GETTER method
#         return self.__age
    
#     def set_age(self, age):        # SETTER method
#         if age >= 0:
#             self.__age = age
#         else:
#             print("Invalid age. Age cannot be negative.")

# list=Student("John",20,"A")
# print("Person age is: ",list.get_age()) # Accessing private attribute via GETTER method

# #print(list.set_age(33)) # Trying to set a negative age via SETTER method

# #print(list.Student.__name)  # Accessing private attribute using name mangling
# list.set_age(-33) # Setting a valid age via SETTER method
# print("Updated Person age is: ",list.get_age()) # Accessing updated age via GETTER method

#******************************** Real World Example of Encapsulation in OOP **************************

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name            # Private attribute
        self.roll_no=roll_no      # Private attribute
        self.__marks=marks          # Private attribute
    
    def get_marks(self):          # GETTER method
        return self.__marks
    
    def set_marks(self,marks):        # SETTER method
        if 0 <= marks <= 100:
            self.__marks=marks
        else:
            print("Invalid marks. Marks should be between 0 and 100.")
    
    def grade(self):          # Method to determine grade based on marks
        if self.__marks >= 95:
            return 'A+'
        elif self.__marks >= 90:
            return 'A'
        elif self.__marks >= 80:
            return 'B'
        elif self.__marks >= 70:
            return 'C'
        elif self.__marks >= 50:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"{self.name} (Roll No: {self.roll_no}) - Marks: {self.__marks}, Grade: {self.grade()}"
    
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

        
result=Student("Jainam",101,85)
result2=Student("Ruchita",102,92)
result3=Student("Ankita",103,78)
result4=Student("Karan",104,45)

classroom=Classroom()
classroom.add_student(result)
classroom.add_student(result2)
classroom.add_student(result3)
classroom.add_student(result4)

print("All Students in the Classroom:")
classroom.show_all_students()

print("Class Average Marks: ",classroom.class_average()) # Calculating class average
print("Top Student: ",classroom.top_student()) # Finding top student

result.set_marks(30)
result.grade()
print("Student Grade: ",result.grade()) # Accessing grade based on updated marks
print("Student Marks: ",result.get_marks()) # Accessing private attribute via GETTER method
