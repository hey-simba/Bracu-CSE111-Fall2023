

#Task 5
class Train:
  def __init__(self,name,A,B,C,Destination):
    self.name=name
    self.A=A
    self.B=B
    self.C=C
    self.Destination=Destination
    self.li=[]
    print(f"Welcome aboard on {self.name}")
    print(f"Start: {self.A}")
    print(f"Destination: {self.Destination}")
  def addPassenger(self,*passengers):

    for i in passengers:
      print(f"{i.passenger} welcome aboard")
      self.li.append(i)
  def allPassengerDetails(self):
    self.fair=0

    for i in self.li:
          if i.start==None:
            i.start=self.A
          if i.stop==None:
            i.stop=self.Destination
          if i.start==self.A and i.stop==self.B:
             i.fair+=100
          elif i.start==self.A and i.stop==self.C:
             i.fair+=200
          elif i.start==self.B and i.stop==self.C:
             i.fair+=100
          elif i.start==self.A and i.stop==self.Destination:
             i.fair+=300
          elif i.start==self.B and i.stop==self.Destination:
             i.fair+=200
          elif i.start==self.C  and i.stop==self.Destination:
              i.fair+=100

          print(f"Name: {i.passenger},Start: {i.start},Destination:{i.stop},Fair: ${i.fair}")

class Passenger:
  def __init__(self,passenger,start=None,stop=None):
    self.start=start
    self.stop=stop
    self.passenger=passenger
    self.fair=0

t1 = Train('T1-Express','New York','Manhattan','Brooklyn','Boston')
print("1========================")
p1 =Passenger("Naruto")
t1.addPassenger(p1)
p2 = Passenger("Sasuke","Manhattan")
p3 = Passenger("Hinata","Manhattan","Brooklyn")
print("2========================")
t1.addPassenger(p2,p3)
print("3========================")
t1.allPassengerDetails()
print("4========================")
t2 = Train('Europe-Express','London','Paris','Brussels','Turkey')
print("5========================")
p4 =Passenger("Max","London","Brussels")
p5 = Passenger("Eleven","Paris")
p6 = Passenger("Mike","Brussels")
t2.addPassenger(p4,p5,p6)
print("6========================")
t2.allPassengerDetails()