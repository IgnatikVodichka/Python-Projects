fruits = ['apple', 'banana', 'kiwi', 'pineapple', 'peach', 'strawberyy']

for i in range(len(fruits)):
    print(f'{i} and {fruits[i]}')

n = int(input('Enter index of element: '))

if n < len(fruits):
    print(fruits[n])
else:
    print('There is no such element on the list')
