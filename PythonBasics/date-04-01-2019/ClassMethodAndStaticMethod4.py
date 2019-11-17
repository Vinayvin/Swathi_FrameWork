import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

c = Circle(4)
print(c.area())
print(c.circle_area(4))