sum = 0
while True:
    s = input('Please enter number: ')
    if s in ["exit", "quit"]:
        break
    elif s == "sum":
        print(sum)
        sum = 0
        continue
    sum += int(s)
