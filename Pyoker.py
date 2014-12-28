# Pyoker
import pygame
import random
import sys
import collections
import _abcoll
from pygame.locals import *
# init window, runtime
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Video Pyoker")
screen.fill((0,0,255))

#To do:
#Conversion of Ace to 1 or 14
#Conversion of face cards to numerical values

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


class deck(object):

	def __init__(self):
		
		self.deck = [(2, heart), (2, diamond), (2, club), (2, spade), (3, heart), (3, diamond), (3, club), (3, spade), (4, heart), (4, diamond), (4, club), (4, spade), (5, heart), (5, diamond), (5, club), (5, spade), (6, heart), (6, diamond), (6, club), (6, spade), (7, heart), (7, diamond), (7, club), (7, spade), (8, heart), (8, diamond), (8, club), (8, spade), (9, heart), (9, diamond), (9, club), (9, spade), (10, heart), (10, diamond), (10, club), (10, spade), (11, heart), (11, diamond), (11, club), (11, spade), (12, heart), (12, diamond), (12, club), (12, spade), (13, heart), (13, diamond), (13, club), (13, spade), (14, heart), (14, diamond), (14, club), (14, spade)]
		# self.deck = [(2, 'H'), (2, 'D'), (2, 'C'), (2, 'D'), (3, 'H'), (3, 'D'), (3, 'C'), (3, 'D'), (4, 'H'), (4, 'D'), (4, 'C'), (4, 'D'), (5, 'H'), (5, 'D'), (5, 'C'), (5, 'D'), (6, 'H'), (6, 'D'), (6, 'C'), (6, 'D'), (7, 'H'), (7, 'D'), (7, 'C'), (7, 'D'), (8, 'H'), (8, 'D'), (8, 'C'), (8, 'D'), (9, 'H'), (9, 'D'), (9, 'C'), (9, 'D'), (10, 'H'), (10, 'D'), (10, 'C'), (10, 'D'), ('J', 'H'), ('J', 'D'), ('J', 'C'), ('J', 'D'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'D'), ('K', 'H'), ('K', 'D'), ('K', 'C'), ('K', 'D'), ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'D')]
	
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
		deck = []

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

def getHandRanks(hand):
	return [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]

def getHandSuits(hand):
	return [hand[0][1], hand[1][1], hand[2][1], hand[3][1], hand[4][1]]

def countRankMatches(hand):
	count = collections.Counter()
	for rank in hand:
		count[rank[0]] += 1
	return count

def countSuitMatches(hand):
	count = collections.Counter()
	for suit in hand:
		count[suit[1]] += 1
	return count

# Scoring

def checkFlush(hand):
	if len(countSuitMatches(hand)) == 1:
		return True
	else:
		return False

def checkStraight(hand):
	hand = sorted(getHandRanks(hand))
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
	hand = sorted(getHandRanks(hand))
	print hand
	if hand[2] == hand[4]:
		return True, hand[1], hand[2]
	if hand[0] == hand[2]:
		return True, hand[0], hand[3]
	else:
		return False

def checkTwoPairs(hand): #Doesn't work.
	ranks = sorted(getHandRanks(hand))
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
	ranks = sorted(getHandRanks(hand))
	for i in range(2):
		if ranks.count(ranks[i]) == 4:
			return True
		else:
			return False

def checkThreePair(hand):
	ranks = sorted(getHandRanks(hand))
	for i in range(3):
		if ranks.count(ranks[i]) == 3:
			return True
		return False

def checkPair(hand):
	ranks = sorted(getHandRanks(hand))
	print ranks
	for i in range(4):
		if ranks.count(ranks[i]) == 2:
			return True
	return False

def checkHighCard(hand):
	return max(sorted(getHandRanks(hand)))


# print Counter(a=4,b=2,c=0,d=-2)

def drawCard(x, y, card):
	white = (255,255,255)
	pygame.draw.rect(screen, white, (x, y, 100, 150))

# drawCard(10,10,1)

decks = deck()
decks.deck = decks.shuffle()
myHand = hand(decks.drawHand(5))

print myHand.hand
# print decks.drawHand()
# print decks.size
# print len(decks.deck)
# print getHandSuits(myHand.hand)
# print getHandRanks(myHand.hand)
# print countRankMatches(myHand.hand)
# print countSuitMatches(myHand.hand)
# print 'Flush? '
# print checkFlush(myHand.hand)
# print 'Straight?'
# print checkStraight(myHand.hand)
# print 'Full house?'
# print checkFullHouse(myHand.hand)
# print 'Pairs?'
# print checkTwoPairs(myHand.hand)
# print 'Four pair?'
# print checkFourPair(myHand.hand)
# print 'Three pair?'
# print checkThreePair(myHand.hand)
# print 'Pair?'
# print checkPair(myHand.hand)
# print 'High card?'
# print checkHighCard(myHand.hand)

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

def renderCard(position, card):

	#draw card border
	pygame.draw.rect(screen, colors['black'], position)

	#draw card interior
	position = (position[0] + 2 ,position[1] + 2, 96, 146)
	pygame.draw.rect(screen, colors['white'], position)

	#render card rank
	rank = myFont.render(str(card[0]), 1, (0, 0, 0))
	screen.blit(rank, (position[0] + 10, position[1] + 5))
	screen.blit(rank, (position[0] + 75, position[1] + 125))

	#render card suit
	if card[1] == spade or card[1] == club:
		suit = myFont.render(card[1], 1, (0, 0, 0))
	else:
		suit = myFont.render(card[1], 1, (255, 0, 0))
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
print myHand.hand[0]
renderCard(card1, myHand.hand[0])
renderCard(card2, myHand.hand[1])
renderCard(card3, myHand.hand[2])
renderCard(card4, myHand.hand[3])
renderCard(card5, myHand.hand[4])

renderButtons()

# pygame.draw.rect(screen, colors['white'], card2)


# print shuffledDeck

# startGame = input('Draw hand? True/False ')

# if startGame == True:
# 	playerHand = hand(decks.drawHand(5))
# 	print "Your hand is . . . "
# 	print playerHand.hand
# 	cardsHeld = input("Which cards would you like to hold? Reply with numbers 1 - 5 in an array seperated by commas")
# 	print playerHand.hold(playerHand.hand, cardsHeld)


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.ext()
	pygame.display.update()

# deck = [(2, 'H'), (2, 'D'), (2, 'C'), (2, 'D'), (3, 'H'), (3, 'D'), (3, 'C'), (3, 'D'), (4, 'H'), (4, 'D'), (4, 'C'), (4, 'D'), (5, 'H'), (5, 'D'), (5, 'C'), (5, 'D'), (6, 'H'), (6, 'D'), (6, 'C'), (6, 'D'), (7, 'H'), (7, 'D'), (7, 'C'), (7, 'D'), (8, 'H'), (8, 'D'), (8, 'C'), (8, 'D'), (9, 'H'), (9, 'D'), (9, 'C'), (9, 'D'), (10, 'H'), (10, 'D'), (10, 'C'), (10, 'D'), ('J', 'H'), ('J', 'D'), ('J', 'C'), ('J', 'D'), ('Q', 'H'), ('Q', 'D'), ('Q', 'C'), ('Q', 'D'), ('K', 'H'), ('K', 'D'), ('K', 'C'), ('K', 'D'), ('A', 'H'), ('A', 'D'), ('A', 'C'), ('A', 'D')]
   

# shuffledDeck = shuffleArray(freshDeck)

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()

# 	screen.fill(black)
