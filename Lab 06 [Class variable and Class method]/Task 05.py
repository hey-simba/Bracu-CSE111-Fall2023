 

#Task 5
class Student:
    total_students = 0
    bracu_students = 0
    other_inst_students = 0

    def __init__(self, name, dprt, inst="BRAC University"):
        self.name = name
        self.department = dprt
        self.institution = inst
        Student.total_students += 1
        if inst == "BRAC University":
            Student.bracu_students += 1
        else:
            Student.other_inst_students += 1

    @classmethod
    def createStudent(cls, name, department, institution="BRAC University"):
        return cls(name, department, institution)

    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.total_students}")
        print(f"BRAC University Student(s): {cls.bracu_students}")
        print(f"Other Institution Student(s): {cls.other_inst_students}")

    def individualDetail(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Institution: {self.institution}")


Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()