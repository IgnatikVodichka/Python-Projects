# GCD brute force, trying all the possible numbers
num1 = int(input('Please input frist number: '))
num2 = int(input('Please input second number: '))

for i in range(1, num2+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        print(gcd)
