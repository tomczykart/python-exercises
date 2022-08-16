
print('\nTen program sprawdza czy podana liczba jest parzysta czy nieparzysta\n')

while True:
    try:
        number = int(input('\nPodaj liczbe: '))
        break
    except:
        print('\nTo nie jest liczba.\n')

if number % 2 == 0:
    print('\nTo jest liczba parzysta\n')
else:
    print('\nTo jest liczba nieparzysta\n')
