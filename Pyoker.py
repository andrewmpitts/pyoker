# Pyoker
import pygame
import random
import sys
from pygame.locals import *
# init window, runtime
# pygame.init()
# screen = pygame.display.set_mode((800,450))
# pygame.display.set_caption("Video Pyoker")
# screen.fill((0,0,255))

J = 11
Q = 12
K = 13
A = 14


class card(object):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

class deck(object):

	def __init__(self):
		
		self.deck = [(2, 'H'), (2, 'D'), (2, 'C'), (2, 'D'), (3, 'H'), (3, 'D'), (3, 'C'), (3, 'D'), (4, 'H'), (4, 'D'), (4, 'C'), (4, 'D'), (5, 'H'), (5, 'D'), (5, 'C'), (5, 'D'), (6, 'H'), (6, 'D'), (6, 'C'), (6, 'D'), (7, 'H'), (7, 'D'), (7, 'C'), (7, 'D'), (8, 'H'), (8, 'D'), (8, 'C'), (8, 'D'), (9, 'H'), (9, 'D'), (9, 'C'), (9, 'D'), (10, 'H'), (10, 'D'), (10, 'C'), (10, 'D'), ('J', 'H'), ('J', 'D'), ('J', 'C'), ('J', 'D'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'D'), ('K', 'H'), ('K', 'D'), ('K', 'C'), ('K', 'D'), ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'D')]
		self.size = len(self.deck)


	def shuffle(self):
		random.shuffle(self.deck)
		return self.deck

	def drawHand(self, size):
		hand = []
		for i in range(size):
			# print self.deck[-1]
			hand.append(self.deck.pop())

			
		return hand

	def newDeck(self):
		self.cardsInDeck = ['2H', '2D', '2C', '2S', '3H', '3D', '3C', '3S', '4H', '4D', '4C', '4S', '5H', '5D', '5C', '5S', '6H', '6D', '6C', '6S', '7H', '7D', '7C', '7S', '8H', '8D', '8C', '8S', '9H', '9D', '9C', '9S', '10H', '10D', '10C', '10S', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QD', 'KH', 'KD', 'KD', 'KS', 'AH', 'AD', 'AC', 'AS']

class hand(object):

	def __init__(self, hand):
		self.hand = hand

	# Designates cards to omit from draw
	def hold(self, hand, cardsHeld):
		newHand = []
		for i in range(len(cardsHeld)):
			newHand.append(hand[i])
		for i in range(5 - len(cardsHeld)):
			newHand.append(decks.drawHand(1))
		return newHand

	def scoreHand(self, hand):
		return True

def getCardRank(card):
	return card[1]

def getCardSuit(card):
	return card[0]

def drawCard(x, y, card):
	white = (255,255,255)
	pygame.draw.rect(screen, white, (x, y, 100, 150))

# drawCard(10,10,1)

decks = deck()
decks.deck = decks.shuffle()
# myHand = hand(decks.drawHand(5))

# print myHand.hand
# print decks.drawHand()
# print decks.size
# print len(decks.deck)


freshDeck = ['2H', '2D', '2C', '2S', '3H', '3D', '3C', '3S', '4H', '4D', '4C', '4S', '5H', '5D', '5C', '5S', '6H', '6D', '6C', '6S', '7H', '7D', '7C', '7S', '8H', '8D', '8C', '8S', '9H', '9D', '9C', '9S', '10H', '10D', '10C', '10S', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QD', 'KH', 'KD', 'KD', 'KS', 'AH', 'AD', 'AC', 'AS']
shuffledDeck = random.shuffle(freshDeck, random.random)



# print shuffledDeck

startGame = input('Draw hand? True/False ')

if startGame == True:
	playerHand = hand(decks.drawHand(5))
	print "Your hand is . . . "
	print playerHand.hand
	cardsHeld = input("Which cards would you like to hold? Reply with numbers 1 - 5 in an array seperated by commas")
	print playerHand.hold(playerHand.hand, cardsHeld)


# while True:
# 	for event in pygame.event.get():
# 		if event.type == QUIT:
# 			pygame.quit()
# 			sys.ext()
# 	pygame.display.update()

# deck = [(2, 'H'), (2, 'D'), (2, 'C'), (2, 'D'), (3, 'H'), (3, 'D'), (3, 'C'), (3, 'D'), (4, 'H'), (4, 'D'), (4, 'C'), (4, 'D'), (5, 'H'), (5, 'D'), (5, 'C'), (5, 'D'), (6, 'H'), (6, 'D'), (6, 'C'), (6, 'D'), (7, 'H'), (7, 'D'), (7, 'C'), (7, 'D'), (8, 'H'), (8, 'D'), (8, 'C'), (8, 'D'), (9, 'H'), (9, 'D'), (9, 'C'), (9, 'D'), (10, 'H'), (10, 'D'), (10, 'C'), (10, 'D'), ('J', 'H'), ('J', 'D'), ('J', 'C'), ('J', 'D'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'D'), ('K', 'H'), ('K', 'D'), ('K', 'C'), ('K', 'D'), ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'D')]
   

# shuffledDeck = shuffleArray(freshDeck)

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

# 	screen.fill(black)
