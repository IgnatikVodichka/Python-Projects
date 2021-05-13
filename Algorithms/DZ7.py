a = int(input('Please enter line "a":  '))
b = int(input('Please enter line "b":  '))
c = int(input('Please enter line "c":  '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Such triangular doesnt exist')

elif a != b and a != c and b != c:
    print('This triangular is "Scalene"')

elif a == b == c:
    print('This triangular is Equilateral')

else:
    print('This triangular is Isosceles')

if c ^ 2 == a ^ 2 + b ^ 2 or a ^ 2 == b ^ 2 + c ^ 2 or b ^ 2 == a ^ 2 + c ^ 2:
    print('This is also a "Right triangular"')
