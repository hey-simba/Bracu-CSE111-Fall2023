 

#Task3
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f'Vector <{self.x}, {self.y}, {self.z}> has been created.')

v1 = Vector3D(2, -3, 1)
magnitude= (v1.x ** 2 + v1.y ** 2 + v1.z ** 2) ** 0.5
print(f"Magnitude of the first vector = {magnitude}")
v2 = Vector3D(-1, 4, 0)
magnitude= (v2.x ** 2 + v2.y ** 2 + v2.z ** 2) ** 0.5
print(f"Magnitude of the second vector = {magnitude}")

dot_product= (v1.x*v2.x)+(v1.y*v2.y)+(v1.z*v2.z) #a1 b1 + a2 b2 + a3 b3
print(f"Dot product of the two vectors = {dot_product}")

cross_x= (v1.y*v2.z)- (v1.z*v2.y)
cross_y= (v1.z*v2.x)- (v1.x*v2.z)
cross_z= (v1.x*v2.y)-(v1.y*v2.x)
v3= Vector3D(cross_x,cross_y,cross_z)
#print(f"Vector <{cross_x},{cross_y},{cross_z}> has been created.")#a2b3 - a3b2, a3b1 - a1b3, a1b2 - a2b1
print(f"Cross product of the two vectors = <{cross_x},{cross_y},{cross_z}>")