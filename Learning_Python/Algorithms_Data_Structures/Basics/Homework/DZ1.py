

x = 5
y = 6

print(f'x = {x} in decimal number system and x = {bin(x)} in binary number system')
print(f'x = {y} in decimal number system and x = {bin(y)} in binary number system')

print(f'{x} AND {y} = {x & y} = {bin(x & y)}')
print(f'{x} OR {y} = {x | y} = {bin(x | y)}')
print(f'{x} XOR {y} = {x ^ y} = {bin(x ^ y)}')
print(f'x = {x} NOT = {~x} = {bin(~ x)}')
print(f'y = {y} NOT = {~y} = {bin(~ y)}')

print(f'{x} = x >> 2 = {x >> 2} = {bin(x >> 2)}')
print(f'{x} = x << 2 = {x << 2} = {bin(x << 2)}')
print(f'{y} = y >> 2 = {y >> 2} = {bin(y >> 2)}')
print(f'{y} = y << 2 = {y << 2} = {bin(y << 2)}')
