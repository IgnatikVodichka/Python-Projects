# how to get all the digits from a number

num = int(input('Enter any whole number: '))

while num > 0:
    print(num % 10)
    num //= 10
