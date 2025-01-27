

#Task2
def chillox(name,place="Mohakhali"):
      meal_dict={"BBQ Chicken Cheese Burger": 250, "Beef Burger": 170, "Naga Drums": 200}
      meal_cost= meal_dict[name]
      delivery_fee=0
      if place=="Mohakhali" or place=="":
        delivery_fee= 40
      else:
        delivery_fee=60
      tax= meal_cost*0.08
      total= meal_cost+ delivery_fee+tax
      print(total)
n= input("Please order your meal: ")
p= input("Please enter your area:")
chillox(n,p)