import math
from math import pi


def AreaOfCircle(x):
    global pi
    s = pi * (x ** 2)
    print(round(s, 2))


AreaOfCircle(5)
