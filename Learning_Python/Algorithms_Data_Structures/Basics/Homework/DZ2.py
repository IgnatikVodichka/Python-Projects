

x1 = float(input(' Please input x1 for function: '))
y1 = float(input(' Please input y1 for function: '))


x2 = float(input(' Please input x2 for function: '))
y2 = float(input(' Please input y2 for function: '))

if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'k = {k}')
    print(f'b = {b}')
    print(f'y = {k:.2f}x + {b:.2f}')
