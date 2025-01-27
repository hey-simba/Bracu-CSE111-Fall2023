 

#task 4
class Shopidify:
  def __init__(self,name = "Guest"):
    self.name = name
    self.di = {}
    if name == 'Guest':
      print('Welcome to Shopidify')
    else:
      print(f'Welcome {self.name} to Shopidify')
  def add_to_cart(self,product, q = 1):
    if q == 1:
      if type(product) == str:
        if product not in self.di:
          self.di[product] = q
        else:
          self.di[product] += q
      elif type(product) == list:
        p_l = []
        q_l = []
        for i in product:
          if type(i) == str:
            p_l.append(i)
          elif type(i) == int:
            q_l.append(i)
        for i in range(len(p_l)):
          if p_l[i] not in self.di:
            self.di[p_l[i]] = q_l[i]
          else:
            self.di[p_l[i]] += q_l[i]
    else:
       if product not in self.di:
          self.di[product] = q
       else:
          self.di[product] += q
  def display_cart(self):
    print(f'Items in the cart for {self.name}:')
    for i,j in self.di.items():
      print(f'-{i}: {j}x')
  def checkout(self):
     if self.name == 'Guest':
        print('Checkout completed for Guest ')
     else:
        print(f'Checkout completed for {self.name}')
  def display_history(self):
        print(f'Purchase history for {self.name}:')
        print("Transaction 1:")
        for i,j in self.di.items():
            print(f'-{i}: {j}x')


guest_account = Shopidify()
print("1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account = Shopidify("John")
print("2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan", 2)
guest_account.add_to_cart("Luffy Action Figure")
guest_account.display_cart()
print("3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.add_to_cart(["Chocolate Chip Cookies", 3,"Goku Action Figure",2,"Dumbbells-5kg",2])
john_account.display_cart()
print("4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.add_to_cart("Air Jordan")
guest_account.display_cart()
print("5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.checkout()
print("6xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
guest_account.display_history()
print("7xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.checkout()
print("8xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
john_account.display_history()
print("9xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")