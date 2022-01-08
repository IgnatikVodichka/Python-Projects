


num = int(input('Please enter number: '))

odd = 0
even = 0

while num > 0:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    num = num // 10

print(f'Odd numbers {odd}')
print(f'Even numbers {even}')
