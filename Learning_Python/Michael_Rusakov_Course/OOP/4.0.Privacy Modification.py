

class Point:
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __test(self):
        print("Private method")

    def runPrivateMethod(self):
        self.__test()


p = Point(10, 15)

# print(p.__x) Wrong, we can't get this parameter because it's private
print(f"x = {p.getX()}")
print(f"y = {p.getY()}")

p.setX(5)
p.setY(7)
print(f"Now x = {p.getX()}")
print(f"Now y = {p.getY()}")


# p.__test() Wrong, we can't execute this method because it's private

p.runPrivateMethod()
