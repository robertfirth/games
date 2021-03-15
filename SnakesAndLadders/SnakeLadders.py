import pygame
from random import random
from pygame.locals import *
from random import *


resolution = (400,300)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen = pygame.display.set_mode(resolution)

#Player1 = input "Please enter your name"
#Player2 = input "Please enter your name"


# game constants
SHOW_SNAKES = True  # snakes 
NUMBER_OF_PLAYERS = 2  # snakes 
MAX_NUMBER_OF_TURNS = 10  # give up after 10 throws: higherst player wins 
NUMBER_OF_SNAKES = 4  # snakes 
NUMBER_OF_LADDERS = 5 # ladders
SIZE_OF_BOARD = 100 # How Many tiles to go through
FINISH_SQUARE_EXACT = True
NUMBER_OF_DICE = 2
BONUS_ROLLS = True
BONUS_ROLLS_ODDS_NUMBER = 5 # deducted so don't add a minus
BONUS_ROLLS_EVENS_NUMBER = 10
GAMES_IN_MATCH = 5
SLIVERING_EFFECT = True # The snakes tongues in out or sound 
SLIVERING_EFFECT_FREQUENCY = 10
LADDER_EFFECT = True # The ladders might wobble
INSULT_BANK = True # do we attack the loser with stupid comments
INSULT_BANK_DIR = True
PRAISE_BANK = True # do we praise the winner with banal comments
PRAISE_BANK_DIR = True
DICE_SIDES = 6 # You can get bigger dice I suppose
PASSWORD = "Rattle"


# Loop through number of snakes/ ladders build array between the two.  The drop will mean a different snake too.  Meaner snake for bigger drop

#for Snake in range(NUMBER_OF_SNAKES)

Snake=1
while Snake <= NUMBER_OF_SNAKES:   
    Snake+=1
    Snake_Bottom= (randint(1, SIZE_OF_BOARD-3))
    Snake_Top =  (randint((Snake_Bottom+1),SIZE_OF_BOARD))
    print ("Snake_Bottom: ",Snake_Bottom, " Snake_Top:", Snake_Top)

Throw=0
Dice=1
DiceScore=0
while Dice <= NUMBER_OF_DICE:
    Dice+=1
    DiceScore=randint(1, DICE_SIDES)    
    Throw +=DiceScore
    print("Dice Roll: ", DiceScore)
    

Player1Location=1
print ("Throw Score:", Throw)
if(Throw % 2 == 0 and BONUS_ROLLS):
    print("{0} is an Even Number, Bonus 10 Points!".format(Throw))
    Throw+=BONUS_ROLLS_EVENS_NUMBER
else:
    print("{0} is an Odd Number, Boobie minus ",BONUS_ROLLS_ODDS_NUMBER," Points".format(Throw))
    if (Throw>BONUS_ROLLS_ODDS_NUMBER):
        Throw-=BONUS_ROLLS_ODDS_NUMBER
    else: 
        Throw=1
print ("Throw Score:", Throw)
Player1Location+=Throw

#loop while location <> SIZE_OF_BOARD and turns less than MAX_NUMBER_OF_TURNS
if(Player1Location == SIZE_OF_BOARD):
    print ("Winner!  you got to " ,SIZE_OF_BOARD)
    print ("Checking number of games won so far...")