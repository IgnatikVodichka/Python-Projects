

for i in range(32, 128):
    # (end ='') used to not start from a next paragraph
    print(f'\t{i} - {chr(i)}', end='')
    if i % 10 == 1:
        # using empty print statement to start from the next paragraph. i % 10 == 1 because we are starting
        # from 32 and the 10th element will be 41 which will give 1 in the modulus.
        print()
