import sys


# default value of recursion stack limit is 1000. We incrised it to 3000 here. Need to be careful with it so that IDE will not crush with critical error
sys.setrecursionlimit(3000)

# Ackermann's recursion function


def Ackfunc(m, n):
    if m == 0:
        return n+1

    elif m > 0 and n == 0:
        return Ackfunc(m-1, 1)

    # we have written here without 'elif' or 'else' because if first 2 'ifs' will be True than 3rd line in function will not be executed
    return Ackfunc(m-1, Ackfunc(m, n-1))


print(Ackfunc(3, 8))
