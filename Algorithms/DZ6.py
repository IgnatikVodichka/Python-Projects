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
