import random
from random import *

set1 = {int(random()*10) for i in range(1, 11)}
set2 = {int(random()*10) for i in range(1, 11)}

set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)
