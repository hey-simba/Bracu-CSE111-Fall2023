 

#Task 2

class Student:
    def __init__(self,name,id,cgpa):
      self.name= name
      self.__id=id
      self.__cgpa=cgpa
    def get_id(self):
      return self.__id
    def get_cgpa(self):
      return self.__cgpa
    def setId(self,x):
      self.__id=x
class Department:
    def __init__(self,dprt):
        self.dprt=dprt
        self.li_student=[]

    def findStudent(self,id):
      found= False
      student= None
      for i in self.li_student:
        if i.get_id()==id:
          found= True
          student= i
          break
      if found:
          print("Student info:")
          print(f"Student Name: {student.name}")
          print(f"ID: {student.get_id()}")
          print(f"CGPA: {student.get_cgpa()}")
      else:
        print(f"Student with this ID doesn't exist, Please give a valid ID")

    def addStudent(self, *obj):
        for i in obj:
          for j in self.li_student:
            if i.get_id()==j.get_id():
              print(f"Student with the same ID already exists, Please try with another ID")
              break

          else:
            self.li_student.append(i)
            print(f"Welcome to {self.dprt} department, {i.name}")
    def details(self):
      print(f"Department Name:{self.dprt}")
      print(f"Number of student: {len(self.li_student)}")
      print("Details of the students:")
      for i in self.li_student:
            print(f"Student name: {i.name}, ID: {i.get_id()}, cgpa: {i.get_cgpa()}")
s1 = Student("Akib", 22301010, 3.29)
s2 = Student("Reza", 22101010, 3.45)
s3 = Student("Ruhan", 23101934, 4.00)
print("1==================================")
cse = Department("CSE")
cse.findStudent(22112233)
print("2==================================")
cse.addStudent(s1,s2,s3)
print("3==================================")
cse.details()
print("4==================================")
cse.findStudent(22301010)
print("5==================================")
s4 = Student("Nakib",22301010,3.22)
cse.addStudent(s4)
print("6==================================")
s4.setId(21201220)
cse.addStudent(s4)
print("7==================================")
cse.details()
print("8==================================")
s5 = Student("Sakib",22201010,2.29)
cse.addStudent(s5)
print("9==================================")
cse.details()