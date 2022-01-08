

n = 9
default_value = 1

for i in range(n):
    print(' '*(n-1) + '#'*default_value + '  ' + '#'*default_value)
    default_value += 1
    n -= 1
