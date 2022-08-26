class GameEngine:

    def __init__(self, playerOne, playerTwo, score, playerOnePick, playerTwoPick):
        #self.choices = choices #{'rock':0, 'paper':1, 'scissors': 2}
        self.playerOne = playerOne
        self.playerTwo = playerTwo
        self.playerOnePick = 0
        self.playerTwoPick = 0
        self.score = {'player1': 0, 'player2':0, 'tie':0}


    def playerName(self):
        self.name = input('Imie:')
        return self.name

    def playerChoice(self):
        while True:
            try:
                self.choice = int(input('Choose rock [1], paper [2], or scissors [3]:'))
                if self.choice > 0 and self.choice < 4:
                    print(f'You have picked:{self.choice}')
                    break
                else:
                    print('wrong choice')
            except:
                print('wrong choice')
        return self.choice

    def findWinner(self):
        if self.playerOnePick == self.playerTwoPick:
            print('It is a TIE')
            self.score['tie'] += 1
        if self.playerOnePick > self.playerTwoPick and self.playerOnePick - self.playerTwoPick == 1:
            print(f'Player one - {self.playerOne} has won\n')
            self.score['player1'] += 1
        if self.playerOnePick < self.playerTwoPick and self.playerTwoPick - self.playerOnePick == 1:
            print(f'Player two - {self.playerTwo} has won\n')
            self.score['player2'] += 1
        if self.playerOnePick < self.playerTwoPick and self.playerTwoPick - self.playerOnePick == 2:
            print(f'Player one - {self.playerOne} has won\n')
            self.score['player1'] += 1
        if self.playerOnePick > self.playerTwoPick and self.playerOnePick - self.playerTwoPick == 2:
            print(f'Player two - {self.playerTwo} has won\n')
            self.score['player2'] += 1


    def showScore(self):
        print(self.score)

    def playGame(self):
        print('Player One is picking now:')
        engine.playerOnePick = engine.playerChoice()
        print('Player Two is picking now:')
        engine.playerTwoPick = engine.playerChoice()
        engine.findWinner()
        engine.showScore()


#make an instance of class GameEngine
engine = GameEngine('player one', 'player two',{},0,0)

#assign players
engine.playerOne = engine.playerName()
engine.playerTwo = engine.playerName()
print(f'\nplayer 1 name:{engine.playerOne}\n, player 2 name:{engine.playerTwo}\n')

#first game
engine.playGame()

#do you want to play again?
while True:
    if input('Do you want to play again? type [y] if yes') == 'y':
        engine.playGame()
    else: break

#show the final score
print(f'\nFinal score is:{engine.score}')
