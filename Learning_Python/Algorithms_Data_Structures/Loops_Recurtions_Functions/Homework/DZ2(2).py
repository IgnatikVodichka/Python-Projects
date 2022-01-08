


num = input('Please enter number: ')
even = odd = 0

for i in num:
    if i in {'0', '2', '4', '6', '8'}:
        even += 1
    else:
        odd += 1

print(f'Qty of Odd numbers: {odd} ; Qty of Even numbers: {even}')
