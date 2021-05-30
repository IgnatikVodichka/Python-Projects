from datetime import *
from time import *

print('Please enter year, month, and day of your birthday:')

user_year = int(input('Please enter "Year" in format YYYY only numbers:'))
user_month = int(input('Please enter "Month" in format MM only numbers:'))
user_day = int(input('Please enter "Day" in format DD only numbers:'))
user_birthday = date(user_year, user_month, user_day)

print(user_birthday)

seconds = (date.today() - date(user_year, user_month, user_day)).total_seconds()
print(f'You are living for {seconds} seconds')
