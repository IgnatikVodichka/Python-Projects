str1 = 'abc'
str2 = 'xyz'
print('Concatenation of strings =', str1 + str2)  # addition of strings

print()

# this will not be an integer when user enters it, it will be a string instead so it will be added like a string
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
print('number1= ', num1)
print('number2= ', num2)
print('Sum of number1 and number 2 as STRINGS ONLY:', num1+num2)

print()

# to make it an integer, a whole number we will need to put INT operator in the veriable
print('Sum of number1 and number 2 as INTEGERS: ', int(num1) + int(num2))

# or we can put INT operator initially before user enters variable, it will already be a whole number when he enters it.
# Keep in mind that if he tries to enter a string (plain text) it will not be accepted by the programm
num3 = int(input('Enter Third Number:'))
print('number3=', num3)
print('Sum of three number: ', num3 + int(num1) + int(num2))

# if we want to have numbers with decimals, we will than have to put FLOAT operator instead of INT
