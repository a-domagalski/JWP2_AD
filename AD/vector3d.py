
class Vector3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        print("Vector3d({}, {}, {})".format(self.x, self.y, self.z))