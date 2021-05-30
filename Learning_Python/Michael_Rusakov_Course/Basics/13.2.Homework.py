
x = input('Please enter first number: ')
y = input('Please enter second number: ')

while True:
    try:
        z = float(x) / float(y)
    except ZeroDivisionError:
        print('Undefined or Infinity')
    else:
        print(z)
    finally:
        exit(0)
