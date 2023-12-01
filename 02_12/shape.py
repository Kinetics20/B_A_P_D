class Shape:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def describe(self):
        print(f'figure in colour {self.colour} and the center in point {self.x, self.y}')

    def distance(self, other_shape):
        distance = ((self.x - other_shape.x) ** 2 + (self.y - other_shape.y) ** 2) ** 0.5
        return distance

    def __str__(self):
        return f'figure in colour {self.colour} and the center in point {self.x, self.y}'


shape1 = Shape(0, 5, "blue")
shape2 = Shape(3, 8, "blue")

shape1.describe()
shape2.describe()

distance_between_shapes = shape1.distance(shape2)
print(f'distance between shapes : {distance_between_shapes}')

print(str(shape1))
print(str(shape2))
