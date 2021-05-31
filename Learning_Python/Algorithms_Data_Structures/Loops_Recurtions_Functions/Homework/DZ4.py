
n = int(input('Please enter length of sum elements: '))
item = 1
summ = 0
for i in range(n):
    summ += item
    item /= -2

print(summ)
