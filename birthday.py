from datetime import date

def get_name():
    name = input('Podaj swoje imie: ')
    return name

def get_age():
    while True:
        try:
            age = int(input('Podaj swój wiek: '))
            break
        except:
            print('\nTo nie jest liczba.\n')
    return age

def calculate_when(age):
    today = date.today()
    today_year = int(today.strftime("%Y"))
    birthday100 = today_year + 100 - age
    return birthday100

name = get_name()
age = get_age()
my100birthday = calculate_when(age)

print(f'\n{name}, Twoje setne urodziny beda w roku {my100birthday}\n')
