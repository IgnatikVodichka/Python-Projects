mydict = dict()
print(mydict)

# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# Dictionaries are written with curly brackets, and have keys and values:
mydict = {'Name': 'John', 'Lastname': 'Doe', 'Age': 35}
print(mydict)
mydict = dict(Name='John', isMale=True)
print(mydict)
# entering the KEY of a dictionary returns value assigned to this key
print(mydict['isMale'])
print(mydict['Name'])

print('___________')

# how to iterate dictionaries with FOR:

for key in mydict:
    print(f'{key} = {mydict[key]}')

mytuple = ('Name', 'isMale')
for key in mytuple:
    print(f'{key} = {mydict[key]}')

print(type(mytuple))

print('______________')

mydict = {i*2: i for i in range(1, 10)}
print(mydict[4])
mydict = {str(i*2): i for i in range(1, 10)}
print(mydict)
