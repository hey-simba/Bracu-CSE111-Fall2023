 

#Task 2
class Farmer:
  def __init__(self, name_id=None):
    self.name_id=name_id
    if name_id==None:
      print(f"Welcome to your farm!")
    elif type(self.name_id) is str:
      print(f"Welcome to your farm, {self.name_id}!")
    else:
      print(f"Welcome to your farm. Your farm ID is {self.name_id} !")
    self.li_crops= []
    self.li_fishes= []
  def addCrops(self, *crops):
    for i in crops:
      self.li_crops.append(i)
    number_crops= len(crops)
    if number_crops>0:
      print(f"{number_crops} crop(s) added.")
    else:
      print(f"No crop(s) added.")
  def addFishes(self, *fishes):
    for i in fishes:
      self.li_fishes.append(i)
    number_fishes= len(fishes)

    if number_fishes>0:
      print(f"{number_fishes} fish(s) added.")
    else:
      print(f"No fish added.")
  def showGoods (self):
    if len(self.li_crops)>0:
      print(f"You have {len(self.li_crops)} crop(s):")
      all_crops= ', '.join(self.li_crops)
      print(all_crops)
    else:
      print(f"You don't have any crop(s).")
    if len(self.li_fishes)>0:
      print(f"You have {len(self.li_fishes)} fish(s):")
      all_fish= ', '.join(self.li_fishes)
      print(all_fish)
    else:
      print(f"You don't have any fish(s).")
f1 = Farmer()
print("-------------------")
f1.addCrops('Rice', "Jute", "Cinnamon")
print("-------------------")
f1.addFishes()
print("-------------------")
f1.addCrops('Mustard')
print("-------------------")
f1.showGoods()
print("-------------------")
f2 = Farmer("Korim Mia")
print("-------------------")
f2.addFishes('Pangash', 'Magur')
print("-------------------")
f2.addCrops("Wheat", "Potato")
print("-------------------")
f2.addFishes("Koi", "Tuna", "Sardine")
print("-------------------")
f2.showGoods()
print("-------------------")
f3 = Farmer(2865127000)
print("-------------------")
f3.addCrops()
print("-------------------")
f3.addFishes("Katla")
print("-------------------")
f3.showGoods()
print("-------------------")