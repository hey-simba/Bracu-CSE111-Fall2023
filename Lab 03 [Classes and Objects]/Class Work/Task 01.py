

#Task 1 part (i)
class  MangoTree:
  def __init__(self,name):
    self.variety= name
    self.height= 1
    self.number_of_mangoes=0

#Driver Code
mangoTree1= MangoTree("Gopalbhog")
print("=====================================")
print("Mango Tree Details:")
print(f"Variety: {mangoTree1.variety}")
print(f"Height: {mangoTree1.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree1.number_of_mangoes}")
print("=====================================")
mangoTree2= MangoTree("Amrapali")
print("Mango Tree Details:")
print(f"Variety: {mangoTree2.variety}")
print(f"Height: {mangoTree2.height} meter(s)")
print(f"Number of mangoes on the tree: {mangoTree2.number_of_mangoes}")
print("=====================================")

#Task 1 part (ii)
class  MangoTree:
  def __init__(self,name):
    self.variety= name
    self.height= 1
    self.number_of_mangoes=0
  def growthUpdate(self, x):
    self.height=self.height+(x*3)
    if (self.variety=="Amrapali"):
      self.number_of_mangoes=self.height*15
    else:
      self.number_of_mangoes= self.height*10
    print(f"Variety:{self.variety}")
    print(f"Height: {self.height} meter(s)")
    print(f"Number of mangoes on the tree: {self.number_of_mangoes}")
#driver code
print("Updated details after 5 years:")
mangoTree1= MangoTree("Gopalbhog")
print("=====================================")
mangoTree1.growthUpdate(5)
print("=====================================")
mangoTree2= MangoTree("Amrapali")
mangoTree2.growthUpdate(5)
print("=====================================")