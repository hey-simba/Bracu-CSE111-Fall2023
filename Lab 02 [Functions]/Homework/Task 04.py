

def username_generator(first_name, last_name, student_id, middle_name=""):
    first_name_upper = first_name[:3].upper()
    last_name_lower = last_name[-3:].lower()
    student_id_str = str(student_id)[-4:]
    middle_name_str = ""
    if middle_name:
        middle_name_str = middle_name
    username = first_name_upper + middle_name_str + last_name_lower + '_' + student_id_str
    return username

first_name = input("First Name: ")
middle_name = input("Middle Name: ")
last_name = input("Last Name: ")
student_id = int(input("Student ID: "))
print(username_generator(first_name, last_name, student_id, middle_name))