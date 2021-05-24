user_dictionary = {'name': 'Ignat', 'age': 28}
print(user_dictionary)
# adding keys and value to the dictionary
user_dictionary.setdefault('isExist', True)
print(user_dictionary)
user_dictionary.pop('name')  # deleting something from the dictionary
print(user_dictionary.get('name'))  # getting velue by asking from the key
print(user_dictionary.keys())  # getting all the keys
print(list(user_dictionary.keys()))  # making list out of keys

user_dictionary['age'] = 35  # same as changing
print(user_dictionary)
user_dictionary['isMale'] = True  # same as add
print(user_dictionary)
user_dictionary.clear()
print(user_dictionary)
