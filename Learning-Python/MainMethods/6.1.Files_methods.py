# 'w' - means that we need to write a file, and if there is no such file it will be created.And if file exsists all it's content will be erased.
# 'x' - means that we want to write in the file and all it's content to be earased but if file doesn't exist, returns error.
# 'a' - means that we want to write in file and whatever we write will be added in the end of the file.
# 'r' - means that we want to read file.
# 'rt' - opens like text file.
# 'rb' - opens file like binary file. (pictures, mp3 files etc...)
handler = open('a.txt', 'w')
handler.write('  abc\nxyz')
handler.close()  # stops working with file.

handler = open('a.txt', 'r')
# '3' in parentheses means how many symbols we want to read from the file.
print(handler.read(3))
print()
# if we write with empty brackets than it will read the remeainder of the file.
print(handler.read())
print()
handler.seek(0)  # python has it's pointer where it stopped reading the file. So with .seek(0), we will reset the pointer to 0, and than we can read whole file again
print(handler.read())

print()

handler.seek(0)  # how to read line by line (iterating with 'for' loop)
for line in handler:
    print(line)


handler.close()
