# key of the dictionary - mutable value
set_x = {'1', '3', '5'}
lst_x = ['2', '4', '6']
# dict_x = {set_x: lst_x}  # this will not work
# dict_x = {lst_x: set_x} # and this will not work either because list and set are mutable objects

# but there is the way

dict_x = {frozenset(set_x): lst_x}
print(dict_x)
dict_y = {tuple(lst_x): set_x}
print(dict_y)

# to get the element's by the key you need to input them exactly how it is in the dictionary
print(dict_y.get(('2', '4', '6')))
print(dict_x.get(frozenset({'3', '5', '1'})))
