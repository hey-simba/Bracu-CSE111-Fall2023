 

#Task 1
class KK_tea:
    total_sales_dict = {}

    def __init__(self, price, tea_bags=50):
        self.price = price
        self.tea_bags = tea_bags
        self.name = "KK Regular Tea"
        self.weight = self.tea_bags * 2
        self.status = False
        if self.name not in KK_tea.total_sales_dict:
            KK_tea.total_sales_dict[self.name] = 0

    def product_detail(self):
        print(f"Name: {self.name}, Weight: {self.weight}")
        print(f"Tea Bags: {self.tea_bags}, Price: {self.price}")
        print(f"Status: {self.status}")

    @classmethod
    def total_sales(cls):
        print(f"Total sales: {KK_tea.total_sales_dict}")

    @classmethod
    def update_sold_status_regular(cls, *args):
        for item in args:
            item.status = True
            KK_tea.total_sales_dict[item.name] += 1

class KK_flavoured_tea(KK_tea):
    def __init__(self, flavour, price, tea_bags):
        super().__init__(price, tea_bags)
        self.name = "KK " + flavour + " Tea"
        self.sell = 0

    @classmethod
    def update_sold_status_flavoured(cls, *args):
        for item in args:
            item.status = True
            if item.name not in KK_tea.total_sales_dict:
                KK_tea.total_sales_dict[item.name] = 1
            else:
                KK_tea.total_sales_dict[item.name] += 1


t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()