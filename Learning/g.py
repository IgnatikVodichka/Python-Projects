i = 0
while i < 10:
    i += 1  # same as we would write i = i + 1
    print('Hello Gay!')

print('End of cycle')

print('--------')

i = 0
while i < 10:
    i += 1
    if i != 5:
        print(i)
print('End of cycle')

print('--------')

i = 0
while i < 10:
    i += 1
    if i == 5:  # same as if command above
        continue
    if i == 8:
        break
    print(i)
print('End of cycle')

print('--------')
s = 1
x = 1
to = 10
while x <= to:  # 10 factorial
    s *= x
    x += 1
print(s)

print('--------')

while True:
    code = input('Enter 0 to exit:  ')
    if code == '0':
        break
print(f'You have entered {0} and exited')
