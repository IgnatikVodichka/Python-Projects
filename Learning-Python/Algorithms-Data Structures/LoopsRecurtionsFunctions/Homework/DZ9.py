num = int(input('Please enter any natural number or press "0" to exit: '))

max_num = 0
max_sum = 0

while num != 0:
    temp_num = num
    temp_sum = 0
    while num > 0:
        temp_sum += num % 10
        num //= 10
    if temp_sum > max_sum:
        max_sum = temp_sum
        max_num = temp_num
    num = int(input('Please enter any natural number: '))
print(f'number {max_num} sum of its digits {max_sum}')
