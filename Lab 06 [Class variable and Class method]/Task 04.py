 

#Task 4
class NikeBangladesh:
    branches = []
    stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    sold = 0

    def __init__(self, branch):
        self.branch=branch
        self.stock = {'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        self.sold = 0
        NikeBangladesh.branches.append(branch)
    @classmethod
    def status(cls):
      print(f"Nike Bangladesh Status:")
      print(f"Branches Opened: {cls.branches}")
      print(f"Currently Stocked {cls.stock}")
      print(f"Sold: {cls.sold}")

    def details(self):
     print(f"Nike {self.branch} outlet:")
     print(f"Products Currently Stocked:{self.stock}")
     print(f"Sold: {self.sold}")

    def restockProducts(self, restock):
      for product,count in restock.items():
        if product in self.stock and product in NikeBangladesh.stock:
          self.stock[product]+=count
          NikeBangladesh.stock[product]+=count
    def productSold(self, sold):
      for product,count in sold.items():
           self.stock[product]-=count
           NikeBangladesh.stock[product]-=count
           self.sold+=count
           NikeBangladesh.sold+=count

print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts(
{"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()