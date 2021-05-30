from datetime import *
from time import *

# that will be the time when the script started. We'll need it later to calculate how much time it took for execution of script.
start = time()

print(date.today())  # year , month and day
print(datetime.today())  # year month day , hours:minutes:seconds.miliseconds

print()

d = date(2025, 7, 27)
print(d)

print()

dt = datetime(2025, 8, 28, 23, 00, 23)
print(dt)
print(dt.year)
print(dt.month)
print(dt.hour)
print(dt.minute)
print(dt.second)

print('--------------------------------')

# lower case letters and upper case letters will return different values.Take care for 'm' - is month, but 'M'- is minutes
print(dt.strftime('%Y.%m.%d %H:%M:%S'))  # formating date and time

print('--------------------------------')

# There is one sapcial object that containes how many seconds passed since 01.01.1970 00:00
print(time())

print('--------------------------------')

# we can put seconds from that date (01.01.1970 00:00) passed and see the date.It also can be negative or positive
spdt = datetime.fromtimestamp(3345454)
print(spdt)
spdt = datetime.fromtimestamp(-3345454)
print(spdt)
# thats the reverse action.It gives how many seconds passed since the date that we input erlier with seconds in brackets
print(spdt.timestamp())

print('--------------------')

print(f'This script took: {time() - start} seconds')
