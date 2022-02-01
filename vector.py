class Vector:

    def __init__(self, *args):
        if len(args) < 3:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        else:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]

    def __str__(self):
        return ('<{0}, {1}, {2}>').format(self.x,self.y, self.z)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        return Vector(new_x, new_y, new_z)

    def magnitude(self):
        return pow(((self.x * self.x) + (self.y * self.y) + (self.z * self.z)), 1/2)

    def scalar(self, other_vector):
        return self.x * other_vector.x + self.y * other_vector.y + self.z * other_vector.z

    def direction_between_vector(self, other_vector):
        numerator = self.scalar(other_vector)
        denominator = self.magnitude() * other_vector.magnitude()
        return numerator/denominator

    def cross(self, other_vector):
        x1, x2 = self.x, other_vector.x # x1 y1 z1
        y1, y2 = self.y, other_vector.y # x2 y2 z2
        z1, z2 = self.z, other_vector.z
        return Vector(y1*z2 - y2*z1, x2*z1 - x1*z2, x1*y2 - x2*y1)

    def dot(self, other_vector):
        x1, x2 = self.x, other_vector.x  # x1 y1 z1
        y1, y2 = self.y, other_vector.y  # x2 y2 z2
        z1, z2 = self.z, other_vector.z
        return x1*x2 + y1*y2 + z1*z2

    def __eq__(self, other_vector):
        angle = self.direction_between_vector(other_vector)
        return True if abs(1 - angle) < 0.00001 else False

    def to_tuple(self):
        return (self.x,
                self.y,
                self.z)


def _main():
    examples = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

    print(Vector(examples[0]).cross(Vector(*examples[1])))
    v1 = Vector([1,2,3])
    v2 = Vector(*[1,2,3])
    print(v1)
    print(v2)
    v3 = v1 + v2
    print(v3)
    print(v1 == v3)
    print(v1 + v2)
    print(v1.cross(v2))
    print(v1.magnitude())
    print(v3.dot(v1))
    print(v1.to_tuple())

    print(v1.x)

if __name__ == "__main__":
    _main()
