print('Hello please enter three numbers to know which one is the greatest number')
a = int(input('Please enter a: '))
b = int(input('Please enter b: '))
c = int(input('Please enter c: '))

if a > b:
    if a > c:
        print(f'Greatest number of three is {a}')
    else:
        print(f'Greatest number of three is {c}')
else:
    if b > c:
        print(f'Greatest number of three is {b}')
    else:
        print(f'Greatest number of three is {c}')
