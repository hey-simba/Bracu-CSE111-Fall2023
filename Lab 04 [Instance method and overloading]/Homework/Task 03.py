 
#Task3
class Department:
  def __init__(self,department="ChE Department", sections= 5):
    self.department=department
    self.sections=sections
    self.students=[]
    print(f"The {self.department} has {sections} sections.")
  def add_students(self, *students):
    for i in students:
      self.students.append(i)
    self.sum= 0
    for i in self.students:
      self.sum+=i
    if len(self.students)== self.sections:
      self.avg= self.sum/ len(self.students)
      print(f"The {self.department} has an average of {self.avg} students in each section.")
    else:
      self.avg=0
      print(f"The {self.department} doesn't have {len(self.students)} sections.")
  def merge_Department(self,*departments_to_merge):
     total_students =0
     for department in departments_to_merge:
        total_students += (department.avg*department.sections)
        print(f'{department.department} is merged to {self.department}.')
     total_students+= (self.avg*self.sections)
     average_students=total_students/self.sections
     self.avg = average_students
     print(f"Now the {self.department} has an average of {average_students} students in each section.")
d1 = Department()
print('1-----------------------------')
d2 = Department('MME Department')
print('2-----------------------------')
d3 = Department('NCE Department', 8)
print('3-----------------------------')
d1.add_students(12, 23, 12, 34, 21)
print('4-----------------------------')
d2.add_students(40, 30, 21)
print('5-----------------------------')
d3.add_students(12, 34, 41, 17, 30, 22, 32, 51)
print('6-----------------------------')
mega = Department('Engineering Department', 10)
print('7-----------------------------')
mega.add_students(21,30,40,36,10,32,27,51,45,15)
print('8-----------------------------')
print(mega.merge_Department(d1, d2))
print('9-----------------------------')
print(mega.merge_Department(d3))