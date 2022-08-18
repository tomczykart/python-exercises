#Checks if the the text is Palindrom

print('\nTell me a word, I will tell you if it is a palindrom:)')

def get_word():
    while True:
        try:
            text = str(input('\nYour word:\n'))
            break
        except:
            print('not a word')
    return text

def reverse_word(word):
        return str(word[::-1])

a = get_word()
b = reverse_word(a)

if a == b:
    print('Palindrom!')
else:
    print('Not a palindrom:(')
