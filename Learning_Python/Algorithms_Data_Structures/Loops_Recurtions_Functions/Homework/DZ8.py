

qty = int(input('Please enter how many numbers will be: '))
digit = int(input('Please eneter digit to look for in numbers: '))
counter = 0

for i in range(1, qty+1):
    num = int(input('Please enter number where to look for:'))
    while num > 0:
        if num % 10 == digit:
            counter += 1
        num //= 10
print(f'The digit {digit} is {counter} times in all of the sequence')


# 2nd solution to this problem:

times = int(input('Please enter how many numbers will be: '))
digits = input('Please eneter digit to look for in numbers: ')
count = 0

for i in range(1, times + 1):
    ans = input(f'Please enter number {i}: ')
    count += ans.count(digits)

print(f'The digit {digits} is {count} times in all of the sequence')
