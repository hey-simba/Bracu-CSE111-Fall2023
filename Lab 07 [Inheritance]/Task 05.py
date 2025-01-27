 

#Task 5
class Employee:
  def __init__(self, name, id, dprt):
    self.name=name
    self.id= id
    self.dprt=dprt
    self.employee_type= "Regular"
    self.salary= 0
    if self.employee_type=="Regular" or self.employee_type=="Foreign":
      self.salary= 30000
    elif self.employee_type=="Part time":
      self.salary= 15000

  def employeeDetails(self):
    print(f"Name: {self.name}, Dept {self.dprt}")
    print(f"Employee id: {self.id}, Salary: {self.salary}")

  def workDistribution(self, dept):
    if dept== "Human Resource":
      print(f"Collect work distribution loads from the manger")
    else:
      print(f"Collect work distribution loads from the HR department.")

  def increment(self):
    if self.employee_type=="Regular":
      self.salary += (self.salary * 0.1)
    elif self.employee_type=="Foreign":
      self.salary += (self.salary* 0.15)




class Foreign_employee(Employee):
  def __init__(self,name, id, dprt):
    super().__init__(name, id, dprt)
    self.employee_type= "Foreign"

  def employeeDetails(self):
    super().employeeDetails()
    print("Employee Type:",self.employee_type)
  def workDistribution(self, dept):
    super().workDistribution(dept)
  def increment(self):
    super().increment()

class Part_time_employee(Employee):
  def __init__(self, name,id, dprt):
     super().__init__(name, id, dprt)
     self.employee_type=="Part time"
  def employeeDetails(self):
    super().employeeDetails()
    print("Employee Type:",self.employee_type)
  def workDistribution(self, dept):
    super().workDistribution(dept)
  def increment(self):
    super().increment()








print("1------------------------------------------")
emp1=Employee("Nawaz Ali", 102, "Marketing")
print("2------------------------------------------")
emp1.employeeDetails()
print("3------------------------------------------")
emp1.workDistribution("Marketing")
print("4------------------------------------------")
emp1.increment()
emp1.employeeDetails()
print("5------------------------------------------")
f_emp=Foreign_employee("Nadvi", 311, "Human Resource")
f_emp.employeeDetails()
print("6------------------------------------------")
f_emp.workDistribution("Human Resource")
print("7------------------------------------------")
f_emp.increment()
f_emp.employeeDetails()
print("8------------------------------------------")
p1_emp=Part_time_employee("Asif", 210, "Sales")
p2_emp=Part_time_employee("Olive", 223, "Accounts")
print("9------------------------------------------")
p1_emp.employeeDetails()
print("10------------------------------------------")
p1_emp.workDistribution("Sales")
print("11------------------------------------------")
p2_emp.increment()
print("12------------------------------------------")
p2_emp.employeeDetails()