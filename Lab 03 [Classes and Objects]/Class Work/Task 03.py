

#TASK-3
class GreenPhone:
    def __init__(self,model_name,version,cameras):
        self.model_name=model_name
        self.version=version
        self.cameras=cameras
        self.company="GreenPhone"
    def showSpecification(self):
        print("Phone Company:",self.company)
        print("Model Name:",self.model_name)
        print("Android Version:",self.version)
        print("Number of Cameras:",self.cameras)
    def updatePhone(self):
        if self.model_name=="A1":
            count1=0
            if count1<=2:
                count1+=1
                self.version+=1
                print(f"Your phone Greenphone {self.model_name} is upgraded to Android Version : {self.version}.")
            else:
                print(f"Your phone Greenphone {self.model} is already up to date.")

        elif self.model_name=="M11":
            count2=0
            if count2<=3:
                count2+=1
                self.version+=1
                print(f"Your phone Greenphone {self.model_name} is upgraded to Android Version : {self.version}.")
            else:
                print(f"Your phone Greenphone {self.model_name} is already up to date.")
        else:
            count3=0
            if count3<=4:
                count3+=1
                self.version+=1
                print(f"Your phone Greenphone {self.model_name} is upgraded to Android Version : {self.version}.")
            else:
                print(f"Your phone Greenphone {self.model_name} is already up to date.")

print('1=======================')
p1 = GreenPhone('A1', 12, 3)
p2 = GreenPhone('M11', 12, 4)
p3 = GreenPhone('U20', 12, 5)
p1.showSpecification()
print('2=======================')
p2.showSpecification()
print('3=======================')
p1.updatePhone()
print('4=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('5=======================')
p1.updatePhone()
p2.updatePhone()
p3.updatePhone()
print('6=======================')
p2.updatePhone()
p3.updatePhone()
print('7=======================')
p1.showSpecification()
p3.showSpecification()