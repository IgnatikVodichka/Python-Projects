

a = int(input('Please enter first number:  '))
b = int(input('Please enter second number:  '))
c = int(input('Please enter third number:  '))

if b < a < c or c < a < b:
    print('First number is middle number')
elif a < b < c or c < b < a:
    print('Second number is middle number')
else:
    print('Third number is middle number')
