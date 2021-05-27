#This is recursion so it can have and Error of stack overflow.
def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)


print(gcd(1701, 3768))
