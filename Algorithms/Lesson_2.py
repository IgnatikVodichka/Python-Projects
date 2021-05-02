# Finding sum and multiplication of three digits of a number of which it consists:
x = int(input('Please Enter a three digit number: '))
a = x // 100
b = x % 100 // 10
c = x % 10

sum = a + b + c
mult = a * b * c

print(f'Sum of numbers of your number = {sum}')
print(f'Multiplication of numbers of your number = {mult}')
