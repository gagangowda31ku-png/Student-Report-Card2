class Student:
    def __init__(self, roll_num, name):
        self.roll_num = roll_num
        self.name = name
        self.__marks = {}

    def get_marks(self):
        return self.__marks
    
    def add_marks(self, subject, marks):
       self.__marks[subject] = marks

    def calc_average(self):
        total = 0
        for marks in self.__marks.values(): 
            total += marks
            average = total/len(self.__marks)

        print(f"{self.name}'s average is {average}")
          
            
            

    def is_passed(self):
        has_passed = all(marks>=35 for marks in self.__marks.values())

        if has_passed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calc_grade(self):
        total = 0
        percentage = (total/(len(self.__marks))*100)*100
                
        if percentage>=90:
            print("GRADE 'A'")
        elif percentage>=70:
            print("GRADE 'B'")
        else:
            print("GRADE 'C'")
    
class Reportcard():
    def generate(self, student:Student):
        student_marks = student.get_marks()
        print(f"Name:{student.name}  , Roll_num:{student.roll_num} ")
        print("---------MARKS-----------")
        for subject, marks in student_marks.items():
            print(f"{subject}-{marks}")
        print("---------------------------")
        student.calc_average()
        student.is_passed()
        student.calc_grade()
class classroom:
    def __init__(self, grade, section):
        self.grade = grade
        self.section = section
        self.__student = []
    
    def add_student(self, student):
        self.__student.append(student)

    def get_student_list(self):
        for i, student in enumerate(student):
            print(f"{i+1} {student.name}")


a = Student(1, "Gagan")
b = Student(2, "Chandan")

a.add_marks("maths", 90)
a.add_marks("physics", 89)


b.add_marks("maths", 67)
b.add_marks("physics", 56)

rc = Reportcard()
rc.generate(a)
rc.generate(b)

cr = classroom(10, "B")
cr.add_student(a)
cr.add_student(b)

cr = classroom(10, "B")
cr.add_student(a)
cr.add_student(b)





            


        



    


