print('\nI will check if your number is prime...')


def get_number():
    while True:
        try:
            number = int(input('\nGive me a number: '))
            break
        except:
            print('\nThat is not a number.\n')
    return number


def check_prime(number):

    #check obvius
    if 1<number <4:
        print('Prime!')
        return True

    if number == 1:
        print('One is not a prime')
        return False

    #check the division by 2
    if not number%2:
        print('Composite number')
        return False

    #check the division by 3
    if not number%3:
        print('Composite number')
        return False

    #range to chceck for number divisors - from 5 to square root of 'number'
    range = int(number**0.5)

    #lets use k6+-1 method, we start to check divisors with 5
    i = 5
    while i <= range:
        if not number%i or not number%(i+2):
            print('Composite number')
            return False
        else: i += 6
    print('Prime!')
    return True

number = get_number()
check_prime(number)
