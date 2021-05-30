def printname():  # you can create your own functions with def(definition) and name them.
    print('Ignat')


printname()  # you can call the function when you need it.


def summa(x, y):  # first we set the parameters of our function.
    return x+y


s = summa(5, 7)  # after we can call for it whenever we want.
print(s)
# or we can call directly as shown here without veriable.
print(f'{summa(5,7)}')

print('_____________')


def multprint(x, y, r=False):
    s = x*y
    if r:
        return s
    else:
        print(s)


# in this case 'r' = False by default in function as we have written it so function only returned the answer back to function.
multprint(22, 10)
# in this case we set 'r' parameter to True so function went further and printed the result.
multprint(22, 10, True)

# We can set parameters as this too.
print(f'{multprint(x=10, y=21, r= True)}')
# If we will not set 'r' veriable, then the output will be 'None' in the terminal, due to two print statements.
#  First is inside function and second is outside function.
#  When a function doesn't return anything, it implicitly returns 'None'.

print('______')
# we use asterix '*' to state that there can be many numbers which we can include.


def bigsum(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s


print(bigsum(1, 3, 4, 5, 6, 2, 3, 4, 5, 8, 9, 7, 6, 5))
# print(bigsum(int(input())))

print('_____________')
# we can use double asterix '**' to include a dcitionary-like parameters


def bigdict(**dict):
    for key in dict:
        print(f'{key} = {dict[key]}')


bigdict(name='Ignat', age=28)

print('_________')
print('Anonymous functions with lambda')


# that's a lambda function also called anonymous function
result = (lambda x, y: (x+y))(8, 9)
print(result)


# example on how to iterate array with one function:

def maxnum(arr):
    max = arr[0]
    for n in arr:
        if n > max:
            max = n
    return max


print(maxnum([1, 2, 3, 4, 5]))
print(maxnum([2, 2, 8, 99, 1232]))
