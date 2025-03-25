#   Create a class (2-D vector) and use it to create another class representing a 3-D vector.


class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    

class Vector3D(Vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z


v2 = Vector2D(1,2)
print(v2.x, v2.y)

v3 = Vector3D(1,2,3)
print(v3.x, v3.y, v3.z)