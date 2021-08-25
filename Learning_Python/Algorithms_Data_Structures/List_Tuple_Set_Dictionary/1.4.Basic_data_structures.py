

# needle in a haystack
t = ('one', 'two')
for i in t:
    print(i)

# here compiler thinks that we have string in the variable and not tuple, because coma ',' is missing.
t = ('one')
# So it will return back letter by letter the whole word
for i in t:
    print(i)

t = ('one',)  # fixed
for i in t:
    print(i)
