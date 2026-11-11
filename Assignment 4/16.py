class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)
    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
v1 = Vector3D(2, 3, 4)
v2 = Vector3D(5, 6, 7)
print("Vector 1:", v1)
print("Vector 2:", v2)
print("Addition:", v1 + v2)
print("Subtraction:", v1 - v2)
print("Dot Product:", v1 * v2)
print("Equality:", v1 == v2)
v3 = Vector3D(2, 3, 4)
print("Equality with v3:", v1 == v3)