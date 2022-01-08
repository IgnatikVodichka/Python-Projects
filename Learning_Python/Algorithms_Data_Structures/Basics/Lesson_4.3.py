

num = int(input('Please enter a number: '))
ans = input('Please enter "b" - for bites and "k" - for kilobites: ')

ans = ans.lower()  # making capital letters accepted for the answer
if ans == 'b':
    print(f"{num} Kb = {num * 1024} bites")
elif ans == 'k':
    print(f"{num} Bites = {num / 1024} Kb")
else:
    print('Wrong entry')
