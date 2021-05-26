try:  # try is trying to do requested option.
    string = float('abc')
# here we are writing an exception to ignore (intercept) the error and in case it's coming up to write what we want.
except ValueError:
    print('Not possible')

while True:  # we can put try inside loops and functions
    a = input('Please enter positive number: ')
    try:
        a = float(a)
        if a <= 0:
            # here we are catching the exception and making our own alert
            raise Exception('This number is not a positive number')
    except ValueError:
        print("That's not correct")
    except Exception as exp:  # here we are calling for the Exception above
        print(exp)
    else:  # try block has else function as well
        print('Thnak you for correct entry')
    finally:  # finally will proceed to carry out no matter what
        print('Wow!')
        exit(0)
