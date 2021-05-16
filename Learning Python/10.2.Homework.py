def checknum(oddnum):
    if oddnum % 2 == 0:
        return True
    else:
        return False


print(checknum(10))


def maxnum(randlist):
    max = randlist[0]
    for n in randlist:
        if n > max:
            max = n
    return max


print(maxnum([1, 2, 3, 4, 5]))


def numaverage(*numbers):
    s = 0
    for n in numbers:
        s += n
        a = s / len(numbers)
    return a


print(numaverage(1, 2, 5, 10, 28, 9))
