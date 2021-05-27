# Euclidean algorithm to find the greatest common divisor
# Subtraction takes a lot of time with big numbers
def gcd(m, n):
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


print(gcd(54, 24))
print(gcd(24, 54))
