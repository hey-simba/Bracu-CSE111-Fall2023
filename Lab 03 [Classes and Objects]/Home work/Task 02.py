

#Task2
class box:
    def __init__(self, dimensions):
        print("Creating a Box!")
        self.height, self.width, self.breadth = dimensions

    def boxDescription(self):
        print("Height:", self.height)
        print("Width:", self.width)
        print("Breadth:", self.breadth)



    def volume(self):
        return (f"Volume of the box is {self.height * self.width * self.breadth} cubic units.")



print("Box 1")
b1 = box([10,10,10])
print("=========================")
b1.boxDescription()
print(b1.volume())
print("-------------------------")
print("Box 2")
b2 = box((30,10,10))
print("=========================")
b2.boxDescription()
print(b2.volume())
b2.height = 300
print("Updating Box 2!")
print("Height:", b2.height)
print("Width:", b2.width)
print("Breadth:", b2.breadth)
volume = b2.height * b2.width * b2.breadth
print(f"Volume of the box is {volume} cubic units.")
print("-------------------------")
print("Box 3")
b3 = b2
b3.boxDescription()
print(b3.volume())


one = (b3 == b2)

b3.width = 100
two = (b3 == b2)