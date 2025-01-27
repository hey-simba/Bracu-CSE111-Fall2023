 

class Store:
    def __init__(self, initial_balance):
        print("New branch created!")
        self.balance = initial_balance
        self.total_items = 0
        self.inventory = {}

    def viewAllItems(self):
        if self.total_items == 0:
            print("There are no items in your inventory")
        else:
            items = ', '.join(self.inventory.keys())
            print(f"All Items: {items}")

    def viewAllItemDetails(self):
        print(self.inventory)

    def add_item(self, item_data):
        item_name, stock, buying_price, selling_price = item_data
        if item_name in self.inventory:
            self.inventory[item_name]['stock'] += stock
        else:
            self.inventory[item_name] = {
                'stock': stock,
                'buying_price': buying_price,
                'selling_price': selling_price,
            }
        self.total_items += 1
        self.balance -= buying_price * stock
        print(f"Item added: {item_name}")
        print(f"Current Balance: {self.balance}")

    def sell_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name]['stock'] >= quantity:
                self.inventory[item_name]['stock'] -= quantity
                revenue = self.inventory[item_name]['selling_price'] * quantity
                self.balance += revenue
                print(f"Sold {quantity} {item_name}(s) for ${revenue}")
            else:
                print(f"Sorry! {item_name} is not available at your desired quantity. Currently we have: {self.inventory[item_name]['stock']}")
        else:
            print(f"Sorry! {item_name} is not available in the inventory.")
        print(f"Current Balance: {self.balance}")

    def restock_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name]['stock'] += quantity
            cost = self.inventory[item_name]['buying_price'] * quantity
            self.balance -= cost
            print(f"Restocked item: {item_name}, Current Stock: {self.inventory[item_name]['stock']}")
            print(f"Current Balance: {self.balance}")
        else:
            print(f"Sorry! {item_name} is not available in the inventory.")

# Driver Code
print("==========================")
branch1 = Store(5000)
print(f"Current Balance: {branch1.balance}")
print(f"Total items: {branch1.total_items}")
branch1.viewAllItems()
branch1.viewAllItemDetails()
print("==========================")
print(f"Current Balance: {branch1.balance}")
branch1.add_item(["ChaCha Noodles", 10, 5, 8])
print(f"Current Balance: {branch1.balance}")
branch1.add_item(["Sparrow Shampoo", 5, 10, 20])
print(f"Current Balance: {branch1.balance}")
print("==========================")
branch1.viewAllItems()
print()
branch1.viewAllItemDetails()
print()
print("==========================")
print(f"Current Balance: {branch1.balance}\n")
branch1.sell_item("ChaCha Noodles", 15)
print(f"Current Balance: {branch1.balance}\n")
branch1.viewAllItemDetails()
print()
branch1.sell_item("ChaCha Noodles", 10)
print()
print(f"Current Balance: {branch1.balance}\n")
branch1.viewAllItemDetails()
print()
print("==========================")
print(f"Current Balance: {branch1.balance}\n")
branch1.restock_item("ChaCha Noodles", 5)
print()
branch1.viewAllItemDetails()
print()
print(f"Current Balance: {branch1.balance}\n")
print("==========================")