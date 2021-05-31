# Tic Tac Toe where 'X' wins from first try:

row = [''] * 3  # created a line(row)
board = [row] * 3  # created a board consisting of 3 rows(lines)
print(board)
print()
# Here we can see that X appeared everywhere in each row in each column.
# That happens because list has 'linked data structures' so list keeps not objects in it self but links to that objects.
# When we made a row we created a list with 3 empty objects, so when we created board it made a link in each row to same objects.
board[0][0] = 'X'
print(board)
print()

# It's better to use list generators for such tasks:
# so now when we add 'X' we will have it only where it intended to be and not in 3 places at a time
board = [[''] * 3 for _ in range(3)]
print(board)
print()
board[0][0] = 'X'
print(board)
