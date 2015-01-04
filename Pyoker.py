# Pyoker
import pygame
import random
import sys
import collections
import _abcoll
# import classes
from pygame.locals import *


# init window, runtime


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Video Pyoker")
screen.fill((0,0,255))

myFont = pygame.font.SysFont("monospace", 18)
suitFont = pygame.font.SysFont("monospace", 30)
buttonFont = pygame.font.SysFont("monospace", 12)

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
handSize = 5

handInPlay = False

colors = {'white':(255, 255, 255), 'black':(0, 0, 0), 'blue':(0, 0, 255), 'red':(255, 0, 0), 'green': (0, 255, 0)}

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

def shuffleDeck(deck):
	random.shuffle(deck)
	return deck

def drawHand(deck, size):
	hand = []
	for i in range(size):
		# print self.deck[-1]
		hand.append(deck.pop())
	return hand

def drawCard(deck):
	return deck.pop()

class deck(object):

	def __init__(self):
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
	def hold(self, cardsHeld):
		newHand = []
		for i in range(len(cardsHeld)):
			newHand.append(self.hand[i])
		for i in range(handSize - len(cardsHeld)):
			newHand.append(drawCard(deck))
		self.hand = newHand
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

def checkHighCard(hand):
	return max(sorted(hand.getRanks()))

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
		return True
	else:
		return False

def checkRoyalFlush(hand):
	if checkFlush(hand) == True and checkStraight(hand) == True:
		return True, checkHighCard(hand)

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


deck = newDeck()
playerHand = hand(drawHand(deck,5))
cardsHeld = set()
# print 'Flush? '
# print checkFlush(playerHand)
# print 'Straight?'
# print checkStraight(playerHand)
# print 'Full house?'
# print checkFullHouse(playerHand)
# print 'Pairs?'
# print checkTwoPairs(playerHand)
# print 'Four pair?'
# print checkFourPair(playerHand)
# print 'Three pair?'
# print checkThreePair(playerHand)
# print 'Pair?'
# print checkPair(playerHand)
# print 'High card?'
# print checkHighCard(playerHand)
# cardsHeld = [0,1,2]
# print playerHand.hold(cardsHeld)
# cardsHeld = []
# print playerHand.getCards()
# print playerHand.hand
# print playerHand.ranks
# print drawCard(deck).card

# GUI

card1 = (50, 200, 100, 150)
card2 = (200, 200, 100, 150)
card3 = (350, 200, 100, 150)
card4 = (500, 200, 100, 150)
card5 = (650, 200, 100, 150)
scoreTable = (25, 25, 750, 150)


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
		suit = suitFont.render(suit, 1, (0, 0, 0))
	else:
		suit = suitFont.render(suit, 1, (255, 0, 0))
	screen.blit(suit, (position[0] + 40, position[1] + 60))
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
	scoredHand = myFont.render("Current Hand's Score: ", 1, (255,255,0))

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
	screen.blit(scoredHand, (487, 45))

	#player score
	playerScoreText = myFont.render("Player Score: " + str(playerScore), 1, (255,255,0))
	screen.blit(playerScoreText, (575, 32))

def renderButtons():
	newHandButtonPos = (50, 400, 100, 25)
	newHandButtonText = buttonFont.render("Draw New Hand", 1, (0, 0, 0))
	holdButtonText = buttonFont.render("Hold", 1, (0, 0, 0))
	unholdButtonText = buttonFont.render("Unhold", 1, (0, 0, 0))
	#draw 'new hand' button
	pygame.draw.rect(screen, colors['black'], (50, 400, 77, 27))
	pygame.draw.rect(screen, colors['white'], newHandButtonPos)
	screen.blit(newHandButtonText, (55, 407))
	# pygame.draw.rect(screen, colors['blue'], newHandButtonPos)

	#draw 'hold' buttons
	# holdButtonPos = (-25, 355, 50, 27)
	buttonXPos =  75
	buttonYPos = 355

	for i in range(handSize):
		pygame.draw.rect(screen, colors['black'], (buttonXPos + 2, 357, 52, 29))
		if playerHand.hand[i].card in cardsHeld:
			pygame.draw.rect(screen, colors['white'], (buttonXPos, buttonYPos, 50, 27))
			screen.blit(unholdButtonText, (buttonXPos + 4, 362))
		else:
			pygame.draw.rect(screen, colors['white'], (buttonXPos, buttonYPos, 50, 27))
			screen.blit(holdButtonText, (buttonXPos + 10, 362))
		buttonXPos += 150
		
def renderHoldAllButton():
	holdAllButtonText = buttonFont.render("Hold All", 1, (0, 0, 0))
	pygame.draw.rect(screen, colors['black'], (245, 400, 77, 27))
	pygame.draw.rect(screen, colors['white'], (245, 400, 75, 25))
	screen.blit(holdAllButtonText, (255, 407))

def renderUnholdAllButton():
	holdAllButtonText = buttonFont.render("Unhold All", 1, (0, 0, 0))
	pygame.draw.rect(screen, colors['black'], (325, 400, 77, 27))
	pygame.draw.rect(screen, colors['white'], (325, 400, 75, 25))
	screen.blit(holdAllButtonText, (329, 407))

def renderDrawButton():
	drawButtonText = buttonFont.render("Draw", 1, (0, 0, 0))
	pygame.draw.rect(screen, colors['black'], (160, 400, 77, 27))
	pygame.draw.rect(screen, colors['white'], (160, 400, 75, 25))
	screen.blit(drawButtonText, (185, 407))

def getMousePos():
	return pygame.mouse.get_pos()

def getClick():
	if pygame.mouse.get_pressed() == (1,0,0):
		print True
	else:
		return False

renderScoreTable(scoreTable)
renderCard(card1, playerHand.hand[0])
renderCard(card2, playerHand.hand[1])
renderCard(card3, playerHand.hand[2])
renderCard(card4, playerHand.hand[3])
renderCard(card5, playerHand.hand[4])

renderButtons()
renderHoldAllButton()
renderDrawButton()
renderUnholdAllButton()

newHandButtonRect = (50, 400, 100, 25)
newHandButtonSize = (100, 25)

holdButtonSize = (50, 27)
holdButtonCordinates = {0:(75, 355), 1:(225, 355), 2:(375, 355), 3:(525, 355), 4:(675, 355)}

drawButtonRect = (160, 400, 77, 27)
drawButtonSize = (77, 27)

unholdAllButtonRect = (325, 400, 75, 25)
unholdAllButtonSize = (75, 25)

holdAllButtonRect = (245, 400, 75, 25)
holdAllButtonSize = (75, 25)

def isRectClicked(dimensions):
	mousePosition = pygame.mouse.get_pos()
	if mousePosition[0] > dimensions[0] and mousePosition[0] < dimensions[0] + dimensions[2]:
		if mousePosition[1] > dimensions[1] and mousePosition[1] < dimensions[1] + dimensions[3]:
			return True

def isHoldButtonClicked():
	#card1
	if pygame.mouse.get_pos()[0] > 75 and pygame.mouse.get_pos()[0] < 125:
		if pygame.mouse.get_pos()[1] > 355 and pygame.mouse.get_pos()[1] < 383:
			return playerHand.hand[0].card
	#card2
	if pygame.mouse.get_pos()[0] > 225 and pygame.mouse.get_pos()[0] < 275:
		if pygame.mouse.get_pos()[1] > 355 and pygame.mouse.get_pos()[1] < 383:
			return playerHand.hand[1].card
	#card3
	if pygame.mouse.get_pos()[0] > 375 and pygame.mouse.get_pos()[0] < 425:
		if pygame.mouse.get_pos()[1] > 355 and pygame.mouse.get_pos()[1] < 383:
			return playerHand.hand[2].card
	#card4
	if pygame.mouse.get_pos()[0] > 525 and pygame.mouse.get_pos()[0] < 575:
		if pygame.mouse.get_pos()[1] > 355 and pygame.mouse.get_pos()[1] < 383:
			return playerHand.hand[3].card
	#card5
	if pygame.mouse.get_pos()[0] > 675 and pygame.mouse.get_pos()[0] < 725:
		if pygame.mouse.get_pos()[1] > 355 and pygame.mouse.get_pos()[1] < 383:
			return playerHand.hand[4].card
	else:
		return False



while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			if isRectClicked(newHandButtonRect) == True: #Checks if 'New Hand' button is clicked
				print True
			if isHoldButtonClicked() != False:
				if isHoldButtonClicked() not in cardsHeld:
					cardsHeld.add(isHoldButtonClicked())
				else:
					cardsHeld.remove(isHoldButtonClicked())
				print cardsHeld
			if isRectClicked(drawButtonRect) == True: #Checks is 'Draw' button is clicked

				print True
			if isRectClicked(unholdAllButtonRect) == True:
				print True
			if isRectClicked(holdAllButtonRect) == True:
				print True
			renderButtons()
		if event.type == QUIT:
			pygame.quit()
			sys.ext()
	pygame.display.update()
