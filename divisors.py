#Create a program that asks the user for a number and then prints out
#a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def get_value():
    while True:
        try:
            value = int(input('\nGive me an integer number, i will give you its divisors\n'))
            break
        except:
            print('\nWrong value\n')
    return value

def find_divisor(value):
    divisors_list = []
    divisors_to_check = range(1,value+1)
    for divisor in divisors_to_check:
        if value % divisor == 0:
            divisors_list.append(divisor)
    return divisors_list

x = get_value()
y = find_divisor(x)
print(y)
