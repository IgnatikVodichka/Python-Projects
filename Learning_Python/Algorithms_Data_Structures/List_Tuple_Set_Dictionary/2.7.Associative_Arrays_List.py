

k = int(input('How many enterprises do you want to be included? '))
enterprises = {}

for i in range(1, k+1):

    name = input('Please enter name of the company: ')
    enterprises[name] = [
        float(input('Planned revenue: ')), float(input('Real revenue: '))]

    enterprises[name].append(enterprises[name][1] / enterprises[name][0])

print('Real revenue is greater than 10, but planned is not done (less then 100%)')

for key, value in enterprises.items():
    if value[1] > 10 and value[2] < 1:
        print(
            f'Enterprise {key} made {value[1]} revenue, which makes {value[2]* 100:.2f}%')
