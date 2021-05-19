# any veriable outside of any function is called 'GLOBAL VARIABLE'
# like so:
x = True
# or
y = 5

# any veriable inside function is called 'LOCAL VARIABLE'


def isOkay(x, y):  # 'x' and 'y' here are local variables therefore they are not accessed by other functions later in the code
    if x == 5:
        y = 3
    return y


print(x, y)  # here we are calling for global 'x' and 'y'

print(isOkay(5, 0))  # here we are calling function and it's local variables


print('-------------------------')


# to re-assign or to use global variable inside function we need to add 'global' in front of variable like so:
def subtraction(x, y):
    global result
    result = x - y
    print(result)  # print should be b4 'return' otherwise it will be unreachable
    return result


result = 0

subtraction(5, 4)
