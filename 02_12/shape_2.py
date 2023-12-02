class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"Figura koloru {self.color} o środku w punkcie ({self.x}, {self.y})"

    def describe(self):
        print(str(self))

    def distance(self, other):
        a2 = (other.x - self.x) ** 2
        b2 = (other.y - self.y) ** 2
        c2 = a2 + b2
        c = c2 ** 0.5
        return c


s1 = Shape(2, 1, "czerwony")
s2 = Shape(6, 4, "zielony")
print(s1.distance(s2))
