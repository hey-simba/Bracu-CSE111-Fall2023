 

class StudentDatabase:
     def __init__(self,name,roll):
         self.name=name
         self.id=roll
         self.grades={}
     def calculateGPA(self,lst,semester):
         total_gpa=0
         sub_lst=[]
         for cha in lst:
             course, grade=cha.split(": ")
             sub_lst.append(course)
             total_gpa+=(float(grade)*3)
         self.grades[semester]={tuple(sub_lst):(total_gpa/((len(sub_lst)*3)))}
     def printDetails(self):
         print(f"Name: {self.name}")
         print(f"ID: {self.id}")
         for key,value in self.grades.items():
              print(f"Courses taken in {key}:")
              for i,j in value.items():
                   for k in i:
                       print(k)
                   print(f"GPA: {j}")
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('---------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('---------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('---------------------------------')
s2.printDetails()