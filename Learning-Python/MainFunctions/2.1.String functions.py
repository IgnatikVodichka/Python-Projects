string1 = 'abc\nxyz'

# r prefix will ask to ignore all special charecters inside string and print it as it is
string2 = r'abc\nxyz'
print(string1)
print(string2)

# .find finds substring in string and returns it's index
print(string1.find('b'))

# also we can specify after which index we want it to look for the substring
print(string1.find('x', 3))

# checking if string actually is a digit or a letter, returns True or False
print(string1.isdigit())

# checking if it's a letter. In this example it will return false because of the symbol \n inside of the string
print(string2.isalpha())
# lower or upper case display of string:
print(string2.lower())
print(string2.upper())

print('------------')

print(ord('a'), ord('z'))  # alphabet starts with code 97 and ends on code 122
print(chr(98))  # that will be 'b'

print('--------------')
# to remove spaces from string we use 'strip'
hello = '       hello        '
print(hello.strip())
hello = '         hello           world           '
# notice how it will not remove spaces between substring inside particular string
print(hello.strip())

print('-------------')

# this function can be use as a format for displaying pre-made stencil and give it values refering to it's index
greetings = 'Hello, {0}. You are {1} old'
print(greetings.format('Ignat', 28))

print('----------')

# and we can use certain parameters like 'name', 'age' instead of indexes:
greetings = 'Hello, {name}. You are {age} old'
print(greetings.format(name='Ignat', age=28))

print('--------')

# we can use tuples too.
user_data = ('Ignat', 30)
greetings1 = 'Hi. {0[0]}, you are {0[1]}'
print(greetings1.format(user_data))

print()

# also you can use this:
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)
# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %. < number of digits > f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation(lowercase/uppercase)

print()

# transforming into digital with reference to first parameter{0:} and then adding code 'd' for transforming into digital format
#  and into binary with 'b' after {0:} :
s1 = 'int: {0:d}; bin: {0:b}'
print(s1.format(5))

print()

# :.3 rounds number to how many digits we need in total.(all together will be 3 digits 0.00(3))
s2 = 'Round up (150 / 47) = {0:.3}'
print(s2.format(150/47))
