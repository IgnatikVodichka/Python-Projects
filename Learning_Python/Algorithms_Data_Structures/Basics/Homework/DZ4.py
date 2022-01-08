

first_letter = input('Please enter first letter:  ')
second_letter = input('Please enter second letter:  ')

first_letter = ord(first_letter) - ord('a')+1
second_letter = ord(second_letter) - ord('a')+1

print(
    f'Index number of the first letter is {first_letter} and second one is {second_letter} ')
print(
    f'Quantity of indexes between them is {abs(first_letter - second_letter)-1}')
