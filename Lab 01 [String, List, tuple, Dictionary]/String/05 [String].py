
#Task5
password= input()
lowercase=True
uppercase=True
digit= True
special= True
special_character="_ , $ , #, @"

for i in password:
    if i.islower():
        lowercase = False
    elif i.isupper():
        uppercase= False
    elif i.isdigit():
        digit= False
    elif i in special_character :
       special= False
if lowercase:
    print("Lowercase character missing",end=", ")
if uppercase:
    print("Uppercase character missing",end=", ")
if digit:
    print("Digit missing",end=", ")
if special:
    print("Special character missing")
if not (lowercase or uppercase or digit or special):
    print("OK")