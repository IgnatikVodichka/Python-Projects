

n = int(input('Please enter a natural number "n": '))
left = 0
for i in range(1, n+1):
    left += i

right = n * (n+1) // 2
print(f'left {left} == {right} right - {left == right}')
