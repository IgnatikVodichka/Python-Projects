import random
# first solution
rn = random.randint(0, 100)
print(rn)
tries = 10
i = 0
while i in range(tries):
    guess = int(input('Guess the number: '))
    if guess == rn:
        print('Bitch You Guessed It!')
        break
    if guess > rn:
        print('Try less')
    else:
        print('Try higher')
    i += 1
else:
    print(f"You haven't guessed it, the number is:{rn}")


# 2nd solution

num = random.randint(0, 100)
print(num)
for i in range(1, 11):
    answer = int(input(f'Try No.{i}. Try to guess the number: '))
    if num < answer:
        print('Aim lower!')
    elif num > answer:
        print('Aim higher!')
    else:
        print(f'You guessed it on the {i} try!')
        break
else:
    print("You haven't guessed it, the number is: {num}")
