a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for number in a:
    if number < 10:
        print(f'{number},')

print([x for x in a if x < 5])