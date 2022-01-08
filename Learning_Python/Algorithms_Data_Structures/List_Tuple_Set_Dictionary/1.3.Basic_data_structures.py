

# same operators but different story:
a = [1, 2, 3, 4, 5]
b = a  # 'b' is assigned the OLD 'a'.That's why it stays same
# here we alocate a new space in memory where NEW 'a' list is created
a = a + [6, 7, 8]
print(a, b)

a = [1, 2, 3, 4, 5]
b = a
a += [6, 7, 8]  # here No NEW list was created
print(a, b)
