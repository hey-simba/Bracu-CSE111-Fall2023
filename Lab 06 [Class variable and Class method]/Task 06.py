 
#Task 6
class SultansDine:
  total_branches= 0
  total_sell= 0
  branches=[]
  @classmethod
  def details(cls):
    print(f"Total Number of branch(s): {cls.total_branches}")
    print(f"Total Sell: {cls.total_sell} Taka")

    if len(cls.branches)!=0:
      for branch in cls.branches:
        print(f"Branch Name: {branch.name}, Branch Sell: {branch.branch_sell} Taka")
        sell_percent= (branch.branch_sell/cls.total_sell)*100
        print(f"Branch consists of total sell's: {sell_percent}% ")

  def __init__(self,name):
    SultansDine.branches.append(self)
    self.name= name
    self.branch_sell=0
    SultansDine.total_branches+=1

  def sellQuantity(self, quantity):
    if 0<quantity<10:
      self.branch_sell= quantity*300
      SultansDine.total_sell+=self.branch_sell
    elif quantity<20:
      self.branch_sell= quantity*350
      SultansDine.total_sell+=self.branch_sell
    else:
      self.branch_sell=quantity*400
      SultansDine.total_sell+=self.branch_sell

  def branchInformation(self):
    print(f"Branch Name: {self.name}")
    print(f"Branch Sell: {self.branch_sell} Taka")

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()