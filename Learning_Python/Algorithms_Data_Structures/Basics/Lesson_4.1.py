

print('Hello please enter three numbers to know which one is the greatest number')
a = int(input('Please enter a: '))
b = int(input('Please enter b: '))
c = int(input('Please enter c: '))
m = a
if m < b:
    m = b
if m < c:
    m = c

print(f'Greatest number of three is {m}')
