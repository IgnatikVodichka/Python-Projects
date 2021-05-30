# my program:
num = int(input('Please enter number: '))
rnum = ''

while num > 0:
    a = num % 10
    num //= 10
    rnum += str(a)

print(f'Reverse number is: {rnum}')

# one more solution to this:

num = input('Please enter number: ')
rnum = ''

for i in num:
    rnum = i + rnum

print(f'Reverse number is: {rnum}')

# classical program (DZ3 in DZ.drawio):

num = int(input('Please enter number: '))
rnum = 0

while num > 0:
    rnum = rnum * 10 + num % 10
    num //= 10

print(f'Reverse number is: {rnum}')


# 'Python style' solution :) :

num = input('Please enter number: ')
rnum = num[::-1]
print(f'Reverse number is: {rnum}')
