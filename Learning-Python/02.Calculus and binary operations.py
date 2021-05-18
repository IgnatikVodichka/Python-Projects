x = 4
y = 2

print("x =", x)
print("y =", y)

# Basic calculus

print("x + y =", x + y)  # addition
print("x - y =", x - y)  # subtraction
print("x * y =", x * y)  # multiplication
print("x / y =", x / y)  # division

# Modulus. remeinder of division (returns what number is left after division)
print("x % y =", x % y)

# floor division. (returns the greatest integer, integer is either less than or equal to the normal division result )
print("x // y =", x // y)

# Exponantiation. Returns first number to the power of second one.
print("x ** y =", x ** y)


# BINARY SYSTEM OPERATIONS AND OTHER

# bin function takes any number and interprets it in binary system as zeros and ones. (starts with '0b')
print("x =", x, "=", bin(x))
# hexodecimal numeral system 16 numbers (starts with '0x')
print("15 =", hex(15))
# octal numeral system (starts with '0o')
print("10 =", oct(10))

print('-------Bitwise--operarions------------')

# Bitwise operations
# OR | sign Sets each bit to 1 if one of two bits is 1
print('x|y=', bin(x | y))

print('x&y=', bin(x & y))  # AND & sign Sets each bit to 1 if both bits are 1

# XOR ^ sign Sets each bit to 1 if only one of two bits is 1
print('x^y=', bin(x ^ y))

print('~x=', bin(~x))  # NOT ~ sign function.Inverts all the bits
print('~x=', ~x)
print('~y=', ~y)

# Signed right shift / Shift left by pushing zeros in from the right and let the leftmost bits fall off / basicly devides number by 2
print('x>>1', bin(x >> 1))

# Zero fill left shift
# Shift right by pushing copies of the leftmost bit in from the left,
# and let the rightmost bits fall off
# basicly multiplies number by 2
print('y<<1', bin(y << 1))

print('x>>1', x >> 1)  # same as upstairs but in decimal number system
print('y<<1', y << 1)  # same as upstairs but in decimal number system
