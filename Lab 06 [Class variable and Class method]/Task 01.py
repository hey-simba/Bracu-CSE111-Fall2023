 

#Task 1
class Student:
  student_no= 0
  def __init__(self,name,dprt,age,cgpa):
    self.name=name
    self.dprt=dprt
    self.age=age
    self.cgpa=cgpa
    Student.student_no+=1

  def showDetails(self):
    print(f"Id: {Student.student_no}")
    print(f"Name:{self.name}")
    print(f"Department: {self.dprt}")
    print(f"Age: {self.age}")
    print(f"CGPA: {self.cgpa}")

  @classmethod
  def from_String(cls,info):
    name,dprt,age,cgpa= info.split("-")
    obj=cls(name,dprt,age,cgpa)
    return obj
s1 = Student("Samin", "CSE", 21, 3.91)
s1.showDetails()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.showDetails()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.showDetails()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.showDetails()

#Subtask 5

#Subtask 6