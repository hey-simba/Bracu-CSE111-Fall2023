 

class Student:
    def __init__(self, name, id, dprt):
        self.name = name
        self.id = id
        self.dprt = dprt
        self.email = None
        self.password = None
        self.login_status = None
        self.advised_courses = []
        print("Student object is created!")
class Usis:
    def __init__(self):
        print("USIS is ready to use!")

    def login(self, student):
        if student.email== None or student.password== None:
            print("Email and password need to be set.")
        else:
            print("Login successful!")
            student.login_status = "Logged in"

    def advising(self, student, *courses):
        if student.login_status != "Logged in":
            print("Please login to advise courses!")
        else:
            if len(courses) == 0:
                print("You haven't selected any courses.")
            else:
                if len(courses) > 3:
                    print("You need special approval to take more than 3 courses.")
                else:
                    student.advised_courses = list(courses)
                    print("Advising successful!")

    def individualDetails(self, student):
        print(f"Name: {student.name}")
        print(f"ID: {student.id}")
        print(f"Department: {student.dprt}")
        advising_courses = ', '.join(student.advised_courses)
        print(f"Advised courses: {advising_courses}")


rakib = Student("Rakib", 12301455, "CSE")
print("1***********************")
usis_obj = Usis()
print("2***********************")
usis_obj.login(rakib)
print("3***********************")
usis_obj.advising(rakib)
print("4***********************")
rakib.email = "rakib@hotmail.com"
rakib.password = "1234"
print("5***********************")
usis_obj.login(rakib)
print("6***********************")
usis_obj.advising(rakib)
print("7***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110", "CSE260")
print("8***********************")
usis_obj.advising(rakib, "CSE110", "PHY111", "MAT110")
print("9***********************")
usis_obj.individualDetails(rakib)