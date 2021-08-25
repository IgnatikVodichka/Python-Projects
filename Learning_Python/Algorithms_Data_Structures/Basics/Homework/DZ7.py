

year = int(input('Please enter a year in such format "YYYY":  '))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print('This year is regular year')
else:
    print('This year is a leap year')
