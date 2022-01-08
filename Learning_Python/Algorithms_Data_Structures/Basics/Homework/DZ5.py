

num = int(input('Please enter index and I will give you its letter (1 - 26):  '))

num = ord('a') + num - 1

print(
    f'Index number of the letter is "{chr(num)}"')
