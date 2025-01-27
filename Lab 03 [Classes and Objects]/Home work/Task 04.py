 

#Task 4
class abcTech:
  def __init__(self,name,designation,department):
    self.name=name
    self.designation= designation
    self.department=department
    self.Skills=[]
    self.Frame=[]
  def printInfo(self):
    print(f"Welcome to abcTech,{self.name}!")
    print(f"Name:  {self.name}")
    print(f"Designation:  {self.designation}")
    print(f"Department: {self.department}")
    skills = ' ,'.join(self.Skills)
    print(f"Programming Skills:{skills} ")
    frames = ' ,'.join(self.Frame)
    print(f"Frameworks: {frames}")

  def addProgrammingSkills(self, skills):
    self.Skills.extend(skills)

  def addFrameworks(self, frame):
    self.Frame.extend(frame)

  def calculateSalary(self, base_salary,hours):
    self.base_salary= base_salary
    self.working_hours=hours
    self.salary=0
    if self.working_hours>144:
      self.salary= self.base_salary+ (hours-144)*800
    else:
      self.salary= self.base_salary
    return self.salary
print("-------------------------")
b1 =abcTech("Tamim Hasan", "Software Engineer", "Android Development")
print("-------------------------")
b1.addProgrammingSkills(["Java", "Python"])
b1.addProgrammingSkills(["Dart", "C++"])
b1.addFrameworks(["Express.js", "React"])
b1.printInfo()
print("-------------------------")
print(f"Your salary for this month is Tk. {b1.calculateSalary(45000, 156)}")
print("-------------------------")
print("-------------------------")
b2 =abcTech("Jahin Khandoker", "Senior Developer", "App Development")
print("-------------------------")
b2.addProgrammingSkills(["Java", "Dart", "Swift"])
b2.addFrameworks(["Flutter", "React Native"])
b2.addFrameworks(["Xamarin"])
b2.printInfo()
print("-------------------------")
print(f"Your salary for this month is Tk. {b2.calculateSalary(103000, 123)}")
print("-------------------------")