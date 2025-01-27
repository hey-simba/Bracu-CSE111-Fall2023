 
#Task 1
class Student:
  def __init__(self,name,cgpa, credit= 9,department="CSE"):
    self.name=name
    self.cgpa=cgpa
    self.credit=credit
    self.department=department
    self.scholarship= " "
  def checkScholarshipEligibility (self):
    if self.cgpa>=3.5 and self.credit>10:
      if self.cgpa >=3.7 :
        self.scholarship= "Merit based scholarship"
        print(f"{self.name} is eligible for Merit based scholarship.")
      else:
        self.scholarship= "Need-based scholarship."
        print(f"{self.name} is eligible for Need-based scholarship.")
    else:
      self.scholarship= " No scholarship "
      print(f"{self.name} is not eligible for scholarship.")

  def showDetails(self):
    print(f"Name: {self.name}")
    print(f"Department: {self.department}")
    print(f"cgpa: {self.cgpa} ")
    print(f"Number of Credits: {self.credit}")
    print(f"Scholarship Status:{self.scholarship}")
print('--------------------------')
std1 = Student("Alif", 3.99, 12)
print('--------------------------')
std1.checkScholarshipEligibility()
print('--------------------------')
std1.showDetails()
print('--------------------------')
std2 = Student("Mim", 3.4)
std3 = Student("Henry", 3.5, 15,"BBA")
print('--------------------------')
std2.checkScholarshipEligibility()
print('--------------------------')
std3.checkScholarshipEligibility()
print('--------------------------')
std2.showDetails()
print('--------------------------')
std3.showDetails()
print('--------------------------')
std4 = Student("Bob", 4.0, 6, "CSE")
print('--------------------------')
std4.checkScholarshipEligibility()
print('--------------------------')
std4.showDetails()