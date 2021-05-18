import MyModule

while True:
    print('1 - Addition ; 2 - Subtraction ; 3 - Multiplication ; 4 - Division ; 5 - To the Power of... ; 0 - Exit ')
    code = input('Please enter option:  ')
    if code == '0':
        exit(0)
    a = float(input('Please enter first number: '))
    b = float(input('Please enter second number: '))
    if code == '1':
        result = MyModule.add(a, b)
    elif code == '2':
        result = MyModule.sub(a, b)
    elif code == '3':
        result = MyModule.mult(a, b)
    elif code == '4':
        result = MyModule.div(a, b)
    elif code == '5':
        result = MyModule.power(a, b)
    print(f'Result is {result}')
