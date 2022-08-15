from datetime import date

name = input('Podaj swoje imie: ')

while True:
    try:
        age = int(input('Podaj swój wiek: '))
        break
    except:
        print('\nTo nie jest liczba.\n')



today = date.today()
today_year = today.strftime("%Y")

birthday100 =  int(today_year) + 100 - int(age)

print(f'\n{name}, Twoje setne urodziny beda w roku {birthday100}\n')
