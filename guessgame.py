import random

class gameEngine:

    def __init__(self, c_number, u_number, count):
        self.c_number = c_number #computer guess value
        self.u_number = u_number #user guess value
        self.count = count #count user guesses

    def computer_guess(self):
        self.c_number = random.randint(1,9) #pick a random value for computer

    def user_guess(self): #let user pick a value
        while True:
            try:
                a = int(input('Pick a numper between 1 and 9:\n'))
                if a > 0 and a < 10:
                    break
            except: print('wrong input\n')
        self.u_number = a

    def compare_results(self): #compere the diffrence in calues
        if self.c_number == self.u_number:
            print(f'\nYou have won after {self.count} attempts!\n')
            self.count = 0
            self.computer_guess()
            return True
        elif self.c_number < self.u_number:
            print('U need to aim lower')
            self.count += 1
            return False
        else:
            print('U need to aim higher')
            self.count += 1
            return False

    def play_game(self):
        engine.computer_guess() #computer Pick
        engine.user_guess() #user pick
        while True: #if u pick incorrect pick again
            b = engine.compare_results()
            if b == False:
                engine.user_guess()
            else: break

engine = gameEngine(0,0,0)

engine.play_game()

while True: #want to play again?
        a = input('Do you want to play again? type [y]')
        if a == 'y':
            engine.play_game()
        else: break
