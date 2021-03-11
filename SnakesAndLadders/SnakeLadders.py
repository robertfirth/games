import pygame
from random import random
from pygame.locals import *



resolution = (400,300)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen = pygame.display.set_mode(resolution)

NumberOfPalyers
Player1 = input "Please enter your name"
Player1 = input "Please enter your name"


# game constants
SHOW_SNAKES = True  # snakes 
NUMBER_OF_SNAKES = 4  # snakes 
NUMBER_OF_LADDERS = 5 # ladders
SIZE_OF_BOARD = 100 # How Many tiles to go through
FINISH_SQUARE_EXACT = True
NUMBER_OF_DICE = 2
BONUS_ROLLS_ODDS = True
BONUS_ROLLS_EVENS = True
BONUS_ROLLS_ODDS_NUMBER = -5
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

ALIEN_ODDS = 22  # chances a new alien appears
BOMB_ODDS = 60  # chances a new bomb will drop
ALIEN_RELOAD = 12  # frames between new aliens
SCREENRECT = pg.Rect(0, 0, 640, 480)
SCORE = 0

#loop through number of snakes/ ladders build array between the two.  The drop will mean a different snake too.  Meaner snake for bigger drop
Snake_Start= random (0)
Snake_End= Snake_Start+random (0)

Ladder_Start
Ladder_End