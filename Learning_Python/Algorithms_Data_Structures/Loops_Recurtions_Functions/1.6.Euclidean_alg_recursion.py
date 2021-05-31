# Recursion function to find GCD
# This is recursion so it can have and Error of stack overflow.

def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)


print(gcd(861, 2345))
