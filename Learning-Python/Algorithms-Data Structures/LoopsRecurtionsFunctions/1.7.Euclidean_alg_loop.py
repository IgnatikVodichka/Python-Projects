# Optimal algorithm to find GCD because it goes through the loop and doesn't have disadvanteges of other 2 algorithms

def gcd(m, n):

    while n != 0:
        m, n = n, m % n
    return m


print(gcd(8, 4))
