# Pyoker
import pygame
import random
import sys
import collections
import _abcoll
import classes
from pygame.locals import *


# init window, runtime


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Video Pyoker")
screen.fill((0,0,255))

J = 11
Q = 12
K = 13
A = 14

#suits
spade = u"\u2660"
club = u"\u2663"
heart = u"\u2665"
diamond = u"\u2666"

#score
playerScore = 0

colors = {'white':(255, 255, 255), 'black':(0, 0, 0), 'blue':(0, 0, 255), 'red':(255, 0, 0), 'green': (0, 255, 0)}
print colors['white']

class Card(object):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.card = (rank, suit)

def newDeck():
	newDeck = []
	for i in [2,3,4,5,6,7,8,9,10,J,Q,K,A]:
		for n in ['heart','diamond','club','spade']:
			newDeck.append(Card(i,n))
	random.shuffle(newDeck)
	return newDeck

def drawHand(deck, size):
	hand = []
	for i in range(size):
		# print self.deck[-1]
		hand.append(deck.pop())

		
	return hand

class deck(object):

	def __init__(self):
		# self.deck = newDeck(self)
		self.deck = [(2, heart), (2, diamond), (2, club), (2, spade), (3, heart), (3, diamond), (3, club), (3, spade), (4, heart), (4, diamond), (4, club), (4, spade), (5, heart), (5, diamond), (5, club), (5, spade), (6, heart), (6, diamond), (6, club), (6, spade), (7, heart), (7, diamond), (7, club), (7, spade), (8, heart), (8, diamond), (8, club), (8, spade), (9, heart), (9, diamond), (9, club), (9, spade), (10, heart), (10, diamond), (10, club), (10, spade), (11, heart), (11, diamond), (11, club), (11, spade), (12, heart), (12, diamond), (12, club), (12, spade), (13, heart), (13, diamond), (13, club), (13, spade), (14, heart), (14, diamond), (14, club), (14, spade)]
		# self.deck = [(2, 'H'), (2, 'D'), (2, 'C'), (2, 'D'), (3, 'H'), (3, 'D'), (3, 'C'), (3, 'D'), (4, 'H'), (4, 'D'), (4, 'C'), (4, 'D'), (5, 'H'), (5, 'D'), (5, 'C'), (5, 'D'), (6, 'H'), (6, 'D'), (6, 'C'), (6, 'D'), (7, 'H'), (7, 'D'), (7, 'C'), (7, 'D'), (8, 'H'), (8, 'D'), (8, 'C'), (8, 'D'), (9, 'H'), (9, 'D'), (9, 'C'), (9, 'D'), (10, 'H'), (10, 'D'), (10, 'C'), (10, 'D'), ('J', 'H'), ('J', 'D'), ('J', 'C'), ('J', 'D'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'D'), ('K', 'H'), ('K', 'D'), ('K', 'C'), ('K', 'D'), ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'D')]
	
		self.size = len(self.deck)


	def shuffle(self):
		random.shuffle(self.deck)
		return self.deck

class hand(object):
	
	def __init__(self, hand):
		self.hand = hand
		self.length = len(hand)
		# self.cards = 

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

	def getCards(self):
		cards = []
		for i in range(len(self.hand)):
			cards.append(self.hand[i].card)
		return cards
		# return self.hand[0]

	def getRanks(self):
		ranks = []
		for i in self.hand:
			ranks.append(i.rank)
		return sorted(ranks)

	def getSuits(self):
		suits = []
		for i in self.hand:
			suits.append(i.suit)
		return suits

	def countRankMatches(self):
		return collections.Counter(self.getRanks())

	def countSuitMatches(self):
		return collections.Counter(self.getSuits())
 


# Scoring

def checkFlush(hand):
	if len(hand.countSuitMatches()) == 1:
		return True
	else:
		return False

def checkStraight(hand):
	hand = sorted(hand.getRanks())
	count = 1
	for i in range(4):
		if hand[i] + 1 == hand[i+1]:
			# print hand[i]
			count += 1
	if count == 5:
		return True, hand[4]
	else:
		return False, hand[4]

def checkFullHouse(hand):
	hand = sorted(hand.getRanks())
	print hand
	if hand[2] == hand[4]:
		return True, hand[1], hand[2]
	if hand[0] == hand[2]:
		return True, hand[0], hand[3]
	else:
		return False

def checkTwoPairs(hand):
	ranks = sorted(hand.getRanks())
	pair = []
	print ranks
	for i in range(len(ranks)):
		if ranks.count(ranks[i]) == 2:
			pair.append(ranks[i])
	if len(set(pair)) == 2:
		return True
	else:
		return False

def checkFourPair(hand):
	ranks = sorted(hand.getRanks())
	for i in range(2):
		if ranks.count(ranks[i]) == 4:
			return True
		else:
			return False

def checkThreePair(hand):
	ranks = sorted(hand.getRanks())
	for i in range(3):
		if ranks.count(ranks[i]) == 3:
			return True
		return False

def checkPair(hand):
	ranks = sorted(hand.getRanks())
	print ranks
	for i in range(4):
		if ranks.count(ranks[i]) == 2:
			return True
	return False

def checkHighCard(hand):
	return max(sorted(hand.getRanks()))


deck = newDeck()
playerHand = hand(drawHand(deck,5))

print 'Flush? '
print checkFlush(playerHand)
print 'Straight?'
print checkStraight(playerHand)
print 'Full house?'
print checkFullHouse(playerHand)
print 'Pairs?'
print checkTwoPairs(playerHand)
print 'Four pair?'
print checkFourPair(playerHand)
print 'Three pair?'
print checkThreePair(playerHand)
print 'Pair?'
print checkPair(playerHand)
print 'High card?'
print checkHighCard(playerHand)

freshDeck = ['2H', '2D', '2C', '2S', '3H', '3D', '3C', '3S', '4H', '4D', '4C', '4S', '5H', '5D', '5C', '5S', '6H', '6D', '6C', '6S', '7H', '7D', '7C', '7S', '8H', '8D', '8C', '8S', '9H', '9D', '9C', '9S', '10H', '10D', '10C', '10S', 'JH', 'JD', 'JC', 'JS', 'QH', 'QD', 'QC', 'QD', 'KH', 'KD', 'KD', 'KS', 'AH', 'AD', 'AC', 'AS']

shuffledDeck = random.shuffle(freshDeck, random.random)



# GUI

card1 = (50, 200, 100, 150)
card2 = (200, 200, 100, 150)
card3 = (350, 200, 100, 150)
card4 = (500, 200, 100, 150)
card5 = (650, 200, 100, 150)
scoreTable = (25, 25, 750, 150)
myFont = pygame.font.SysFont("monospace", 18)
buttonFont = pygame.font.SysFont("monospace", 12)

def convertSuitToUnicode(suit):
	if suit == 'spade':
		return spade
	if suit == 'club':
		return club
	if suit == 'diamond':
		return diamond
	else:
		return heart

def renderCard(position, card):

	suit = convertSuitToUnicode(card.suit)
	# print suit
	#draw card border
	pygame.draw.rect(screen, colors['black'], position)

	#draw card interior
	position = (position[0] + 2 ,position[1] + 2, 96, 146)
	pygame.draw.rect(screen, colors['white'], position)

	#render card rank
	rank = myFont.render(str(card.rank), 1, (0, 0, 0))
	screen.blit(rank, (position[0] + 10, position[1] + 5))
	screen.blit(rank, (position[0] + 75, position[1] + 125))

	#render card suit
	if suit == spade or suit == club:
		suit = myFont.render(suit, 1, (0, 0, 0))
	else:
		suit = myFont.render(suit, 1, (255, 0, 0))
	screen.blit(suit, (position[0] + 40, position[1] + 66))
	# screen.blit(suit, position)


def renderScoreTable(position):

	#draw border
	pygame.draw.rect(screen, colors['white'], position)
	
	#draw window
	position = (position[0] + 5 ,position[1] + 5, 740, 140)
	pygame.draw.rect(screen, colors['blue'], position)

	#score text variables
	royalFlush = myFont.render("Royal Flush: 200", 1, (255,255,0))
	straightFlush = myFont.render("Straight Flush: 175", 1, (255,255,0))
	fourKind = myFont.render("Four of a Kind: 150", 1, (255,255,0))
	fullHouse = myFont.render("Full House: 125", 1, (255,255,0))
	flush = myFont.render("Flush: 100", 1, (255,255,0))
	straight = myFont.render("Straight: 75", 1, (255,255,0))
	threeKind = myFont.render("Three of a Kind: 50", 1, (255,255,0))
	twoPair = myFont.render("Flush: 25", 1, (255,255,0))
	pair = myFont.render("Pair: 10", 1, (255,255,0))
	nothing = myFont.render("Nothing: -25", 1, (255,255,0))

	#draw hand scores
	screen.blit(royalFlush, (40, 32))
	screen.blit(straightFlush, (40, 46))
	screen.blit(fourKind, (40, 60))
	screen.blit(fullHouse, (40, 74))
	screen.blit(flush, (40, 88))
	screen.blit(straight, (40, 102))
	screen.blit(threeKind, (40, 116))
	screen.blit(twoPair, (40, 130))
	screen.blit(pair, (40, 144))

	#player score
	playerScoreText = myFont.render("Player Score: " + str(playerScore), 1, (255,255,0))
	screen.blit(playerScoreText, (575, 32))

def renderButtons():
	newHandButtonPos = (50, 400, 100, 25)
	newHandButtonText = buttonFont.render("Draw New Hand", 1, (0, 0, 0))
	holdButtonText = buttonFont.render("Hold", 1, (0, 0, 0))
	#draw 'new hand' button
	pygame.draw.rect(screen, colors['black'], (50, 400, 77, 27))
	pygame.draw.rect(screen, colors['white'], newHandButtonPos)
	screen.blit(newHandButtonText, (55, 405))
	# pygame.draw.rect(screen, colors['blue'], newHandButtonPos)

	#draw 'hold' buttons
	# holdButtonPos = (-25, 355, 50, 27)
	buttonXPos =  75

	for i in range(5):
		pygame.draw.rect(screen, colors['black'], (buttonXPos + 2, 357, 52, 29))
		pygame.draw.rect(screen, colors['white'], (buttonXPos, 355, 50, 27))
		screen.blit(holdButtonText, (buttonXPos + 10, 362))
		buttonXPos += 150


renderScoreTable(scoreTable)
renderCard(card1, playerHand.hand[0])
renderCard(card2, playerHand.hand[1])
renderCard(card3, playerHand.hand[2])
renderCard(card4, playerHand.hand[3])
renderCard(card5, playerHand.hand[4])

renderButtons()


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.ext()
	pygame.display.update()