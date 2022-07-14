class Mark():
    def __init__(self, math, eng, science):
        self.math= math
        self.eng = eng
        self.science = science
    
    def get_total_mark(self):
        return self.math + self.eng + self.science

class Student():
    def __init__(self, name, rollno, age, gender, mark):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.gender = gender
        self.mark = mark

class Display():
    def __init__(self,student):
        self.student = student

    def display_student_details(self):
        print("-----STUDENT-DETAIL----")
        print(f"NAME :{self.student.name}")
        print(f"ROLL_NO : {self.student.rollno}")
        print(f"AGE : {self.student.age}")
        print(f"GENDER : {self.student.gender}")
        print(f"TOTAL_MARK : {self.student.mark.get_total_mark()}")

mark = Mark(60, 70, 65)
std1 = Student("bilal", 8, 21, "male", mark)
display = Display(std1)
display.display_student_details()