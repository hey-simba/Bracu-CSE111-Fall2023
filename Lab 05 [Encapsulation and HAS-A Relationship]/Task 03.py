 

#Task 3
class Spaceship:
  def __init__(self,name,capacity):
    self.name=name
    self.capacity=capacity
    self.cargo_li=[]
    self.current_weight=0

  def load_cargo(self, cargo):
    self.extra_weight=0
    if self.current_weight + cargo.get_weight() <= self.capacity:
       self.cargo_li.append(cargo)
       self.current_weight += cargo.get_weight()
    else:
      self.extra_weight= self.current_weight + cargo.get_weight()-self.capacity
      print(f"Warning: Unable to load {cargo.get_name()} inside {self.name}. Exceeds capacity by {self.extra_weight}.")
  def display_details(self):
    cargo_name = [cargo.get_name() for cargo in self.cargo_li]
    print(f"Spaceship Name:{self.name}")
    print(f"Capacity: {self.capacity}")
    print(f"Current Cargo Weight: {self.current_weight}")
    print(f"Cargo:{cargo_name}")

class Cargo:
  def __init__(self,name,weight):
    self.__name=name
    self.__weight= weight
  def get_name(self):
    return self.__name
  def get_weight(self):
    return self.__weight



falcon = Spaceship("Falcon", 50000)
apollo = Spaceship("Apollo", 100000)
enterprise = Spaceship("Enterprise", 220000)
print("1.===================================")
gold = Cargo("Gold", 20000)
platinum = Cargo("Platinum", 25000)
dilithium = Cargo("Dilithium", 50000)
trilithium = Cargo("Trilithium", 70000)
neutronium = Cargo("Neutronium", 80000)
print("2.===================================")

falcon.load_cargo(gold)
falcon.load_cargo(platinum)
falcon.display_details()
print("3.===================================")
apollo.load_cargo(gold)
apollo.display_details()
print("4.===================================")
falcon.load_cargo(neutronium)
print("5.===================================")
enterprise.load_cargo(dilithium)
enterprise.load_cargo(trilithium)
enterprise.load_cargo(neutronium)
enterprise.display_details()