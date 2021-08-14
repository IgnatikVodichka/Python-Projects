from math import sqrt
from typing import ClassVar


class Point:  # class
    x = 0
    y = 0

    def __init__(self, x=0, y=0):  # constructor.
        self.x = x
        self.y = y

    def distance(self, p):  # method to return distance between two points.
        return sqrt((p.x - self.x) ** 2 + (p.y - self.y) ** 2)

    def __str__(self):  # how we will display this class as a string when we call it.
        return(f"Coordinates of point: ({self.x} ; {self.y})")


class Auto:
    p = Point(0, 0)
    speed = 0

    def __init__(self, p=Point(0, 0), speed=0):
        self.p = p
        self.speed = speed

    def setspeed(self, speed):
        self.speed = speed

    def gettime(self, end_point):
        if self.speed != 0:
            return self.p.distance(end_point) / self.speed
        else:
            return -1


p = Point(5, 5)
print(p)
print(p.distance(Point()))
print(p.distance(Point(3, 10)))

car = Auto()
car.setspeed(50)
print(car.speed)

print(car.gettime(Point(100, 200)))

car.setspeed(0)
print(car.gettime(Point(100, 200)))
