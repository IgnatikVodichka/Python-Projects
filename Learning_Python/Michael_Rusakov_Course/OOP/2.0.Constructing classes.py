

class Circle:
    x = 0
    y = 0
    r = 0

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


c = Circle(5, 7, 10)

print(f"x = {c.x} , y = {c.y}, r = {c.r}")
