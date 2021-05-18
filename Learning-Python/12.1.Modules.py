import math as m  # we can name 'math' module for comfort as another word and then use it
import random
from random import *  # here we imported ALL functions from random with asterix "*" so we don't need to write 'random.' in front of all of them
# returns the sine value of 30 degrees
print(m.sin(m.radians(30)))  # here we use m instead of math already
# if we woudn't have imported ALL trough '*' asterix sign we would have to write it as is : random.randint(1, 20)
print(randint(1, 20))
