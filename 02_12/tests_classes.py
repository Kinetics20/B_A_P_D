class User:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, num_1, num_2):
        return num_1 + num_2


u = User(0, 0)
score = u.addition(5, 10)
print(score)
