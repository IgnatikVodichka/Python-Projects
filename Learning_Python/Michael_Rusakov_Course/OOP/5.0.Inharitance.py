

class Shape:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print(f"{self.x}, {self.y}")

    def draw(self):
        print("Drawing some Shape")


class Circle(Shape):  # new class Circle inharits everything from class Shape
    r = 0

    def __init__(self, x, y, r):
        Shape.__init__(self, x, y)
        self.r = r

    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    w = 0
    h = 0

    def __init__(self, x, y, w, h):
        Shape.__init__(self, x, y)
        self.w = w
        self.h = h

    def draw(self):
        print("Drawing Rectangle")


s = Shape(5, 7)

s.draw()

c = Circle(5, 6, 7)

c.draw()

r = Rectangle(4, 3, 8, 9)

r.draw()

c.printXY()
r.printXY()
