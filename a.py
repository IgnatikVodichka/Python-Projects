arr = [-1, -2, 3, 4, 5, 6, 2, 0]

p = 0
n = 0
z = 0

print(arr)

for i in range(len(arr)):

    if arr[i] > 0:
        p += 1
    elif arr[i] < 0:
        n += 1
    else:
        z += 1


print(f'{p / len(arr):.6f}')
print(f'{n / len(arr):.6f}')
print(f'{z / len(arr):.6f}')
