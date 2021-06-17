array1 = [1, 2, 3]
array2 = [1, 2, 3, 4]
array3 = []

for i in range(len(array1) and len(array2)):
    summ = array1[i] + array2[i]
    array3.append(summ)

print(array3)
