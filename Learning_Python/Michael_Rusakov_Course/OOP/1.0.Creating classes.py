

# creating a class with word 'class' and CamelCase name for your Class.
# Class contains property of the objects which will be created later.
class Point:
    x = 0
    y = 0


# Creating object which is related to this class we created earlier.
point1 = Point()

print(point1)  # printing out object in the console.

print(point1.x, ';', point1.y)  # printing properties of this object.

point1.x = 5  # changing properties of that object.
point1.y = 5

print(point1.x, ';', point1.y)  # printing new properties of object.

print(Point)  # printing class info.

point2 = Point()

point2.z = 10  # adding new properties to another object outside it's CLass, although there was no such property before.

print(point2.x, ';', point2.y, ';', point2.z)

# if we will try to print "point1.z" it will give an error because point1 doesn't have this property.
# same as "point2" doesn't have x and y attributes. x and y are still 0.
