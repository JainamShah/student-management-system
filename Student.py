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