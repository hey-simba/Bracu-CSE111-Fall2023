 

#Task 2

class Foodie:

  def __init__(self,name):
    self.name=name

    self.cart= {}
    self.total_spent=0
    self.waiter_tips=0
  def show_orders(self):

    num_items= len(self.cart)
    items = list(self.cart.keys())
    return f"{self.name} has {num_items} item(s) in the cart.\nItems: {items}\nTotal spent: {self.total_spent}."
  def order(self, *args):
    for order in args:
     food, quantity= order.split("-")
     food= food.strip()
     quantity = int(quantity)
     if food in menu:
         if food in self.cart:
            self.cart[food] += quantity
         else:
            self.cart[food] = quantity
            self.total_spent += menu[food] * quantity
            print(f"Ordered - {food}, quantity - {quantity}, price (per Unit) - {menu[food]}.")
            print(f"Total price - {menu[food] * quantity}")
     else:
                print(f"{food} is not available in the menu.")
  def pay_tips(self, tips=0):
        if tips > 0:
            self.waiter_tips = tips
            self.total_spent += self.waiter_tips
            print(f"Gives {tips}/- tips to the waiter.")
        else:
            print("No tips to the waiter.")
menu = {'Chicken Lollipop':15,'Beef Nugget':20,'Americano':180,'Red Velvet':150,'Prawn Tempura':80,'Saute Veg':200}


f1 = Foodie('Frodo')
print(f1.show_orders())
print('1----------------------')
f1.order('Chicken Lollipop-3','Beef Nugget-6','Americano-1')
print('2----------------------')
print(f1.show_orders())
print('3----------------------')
f1.order('Red Velvet-1')
print('4----------------------')
f1.pay_tips(20)
print('5----------------------')
print(f1.show_orders())
f2 = Foodie('Bilbo')
print('6----------------------')
f2.order('Prawn Tempura-6','Saute Veg-1')
print('7----------------------')
f2.pay_tips()
print('8----------------------')
print(f2.show_orders())