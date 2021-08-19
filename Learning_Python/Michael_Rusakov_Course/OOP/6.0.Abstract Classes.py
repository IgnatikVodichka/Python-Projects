from abc import ABC, abstractmethod
# ABC makes Class abtract
# abstractmethod makes method(def) abstract


class Shape(ABC):
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        '''Returns X and Y'''
        print(f"{self.x}, {self.y}")

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):  # class Circle inharits everything from abstract class Shape
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


c = Circle(10, 15, 25)

c.draw()

r = Rectangle(5, 8, 20, 23)
r.draw()
r.printXY()
