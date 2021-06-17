arr = [1, 2, 3, 4, 5]

indicator = 0
minmax = []

for i in range(len(arr)):
    summ = sum(arr) - arr[i]
    minmax.append(summ)


print(min(minmax), max(minmax))


# while indicator != arr[-1]:
#     summ = sum(arr) - arr[indicator]
#     minmax.append(summ)
#     indicator += 1
#     print(summ)
