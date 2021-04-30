# LESSON No.1

print('Hello World')  # print - displaying string(text) or a number in brackets
print('ABC')
print('2+3')  # if anything put in quotes it will be displayed as a string (text)
print(2+3)  # if without quotes it's a number and it will add it or subtract
print('Hello Mike ' + "and Garfield")  # you can add strings to each other
# you can make space between them with , which is called sep
print('Hello Mike' 'and Garfield')
# you can assign sep whatever you like it to be
print('hello mike', 'and John', sep='abcdef')
# with \ reverse slash you can disregard the quotes and with \n you can put what ever following after to new paragraph
print("hello mike", '\\"' "\nand John")

# LESSON No.2 - VARIABLES

age = (28)  # integer
# You can't add string and inegers together without string variable
print("My age " + str(age))
print("My age", age)  # However You can write them with , together

temp = 36.6  # float
print('My temperature is ' + str(temp), 'Degrees Celcius C')

username = "Ignat"  # string
print(username)

iexist = True  # boolean
print(iexist)
# we can change variable value as we go. But usually it's not recommended to do so. Variable should be assigned for single purpose and not changed.
iexist = False
print("It Exists:", iexist)

print("Type of this veriable is:", type(age))
print("Type of this veriable is:", type(iexist))


''' Three single or doungle quotes
can be used to leave comments
in multiple rows 
however it's not counted as a comment which is made by '#' sign.
Although some developers use it to make comments-like entries inside the code.
'''
