from math import pi, sqrt


class Circle:
    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle about radius {self.r}'

    def describe(self):
        return str(self)

    @classmethod
    def from_area(cls, area):
        radius = sqrt(area / pi)
        return Circle(radius)

    @classmethod
    def from_diameter(cls, d):
        return cls(d / 2)

    @staticmethod
    def area_to_radius(area):
        return sqrt(area / pi)

    def area(self):
        return pi * self.r ** 2

    def circumference(self):
        return pi * self.r * 2


c1 = Circle(5)
print(c1.describe())
print(c1.area())
print(c1.circumference())

c10 = Circle.from_area(10)
print(f'radius circle about area 10 is : {c10.r}')

c6 = Circle.from_diameter(6)
print(f'radius circle about diameter 6 is : {c6.r}')
