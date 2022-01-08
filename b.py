

n = 6
default_value = 1
for i in range(n):
    print(' '*(n-1) + '#'*default_value)
    default_value += 1
    n -= 1


n = int(input("Enter height of stairs: "))


def pyramid(n, i=1):

    if n == 0:
        return

    else:
        print(' '*(n - 1) + '#'*i)
        return pyramid(n - 1, i + 1)


pyramid(n)


k = int(input("Enter number of levels for pyramids: "))


def pyramid(n, k, i=0):

    if n == 0:
        return 0

    else:
        print(k*(" "*(n-1) + "#"*(2*i+1) + " "*(n-1)))
        return pyramid(n-1, k, i+1)


pyramid(n, k)
