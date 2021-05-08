x = 5
y = 6

print(f'x = {x} in decimal number system and x = {bin(x)} in binary number system')
print(f'x = {y} in decimal number system and x = {bin(y)} in binary number system')
print(bin(x | y))
print(bin(x & y))
print(bin(x ^ y))
print(bin(~ x))
print(bin(~ y))
print(bin(x >> 1))
print(bin(1 << x))
print(bin(y >> 1))
print(bin(1 << y))
