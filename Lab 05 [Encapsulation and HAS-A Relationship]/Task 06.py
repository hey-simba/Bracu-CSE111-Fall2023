 

#Task-6
class BracuStudent:
  def __init__(self,name,home):
    self.name=name
    self.home=home
    self.bus_pass=False

  def show_details(self):
    print(f"Student Name: {self.name}")
    print(f"Lives in {self.home}")
    print(f"Have Bus Pass? {self.bus_pass}")

  def get_pass(self):
        if self.bus_pass:
            print("You already have a bus pass!")
        else:
            self.bus_pass = True
class BracuBus:
  def __init__(self,route,cap=2):
    self.route=route
    self.cap=cap
    self.lst=[]
    self.count=0
  def show_details(self):
    print(f"Bus Route: {self.route}")
    print(f"Passengers Count: {len(self.lst)} (Max: {self.cap})")
    print(f"Passengers On Board: {self.lst}")


  def board(self, *students):
   for i in students:
      if self.count < self.cap:
          if not i.bus_pass:
              print(f"{i.name} doesn't have a bus pass!")
          else:
              if self.route == i.home:
                  print(f"{i.name} boarded the bus.")
                  self.lst.append(i.name)
                  self.count += 1
              else:
                   print(f"{i.name} got on the wrong bus!")
      else:
          break

   if len(self.lst) == 0:
      print("No passengers!")
   else:
      print("Bus is full!")


st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()