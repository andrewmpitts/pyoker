# Pyoker
import pygame
import random
import sys
import collections
import _abcoll
import poker
from pygame.locals import *

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,450))
pygame.display.set_caption("Video Pyoker")
screen.fill((0,0,255))

J = 11
Q = 12
K = 13
A = 14

handInPlay = False

#suits
spade = u"\u2660"
club = u"\u2663"
heart = u"\u2665"
diamond = u"\u2666"

#score
playerScore = 0
handSize = 5

#GUI Fonts
myFont = pygame.font.SysFont("monospace", 18)
suitFont = pygame.font.SysFont("monospace", 30)
buttonFont = pygame.font.SysFont("monospace", 12)

#GUI Color
colors = {'white':(255, 255, 255), 'black':(0, 0, 0), 'blue':(0, 0, 255), 'red':(255, 0, 0), 'green': (0, 255, 0), 'grey': (125, 125, 125)}

#GUI Shapes
card1 = (50, 200, 100, 150)
card2 = (200, 200, 100, 150)
card3 = (350, 200, 100, 150)
card4 = (500, 200, 100, 150)
card5 = (650, 200, 100, 150)
scoreTable = (25, 25, 750, 150)


deck = poker.newDeck()
playerHand = poker.hand(poker.drawHand(deck))
discards = set()

def convertSuitToUnicode(suit): #Converts the card suit into Unicode for display in GUI
	if suit == 'spade':
		return spade
	if suit == 'club':
		return club
	if suit == 'diamond':
		return diamond
	else:
		return heart

drawNewHandButtonEnabled = True
holdButtonsEnabled = False
drawButtonEnabled = False
discardAllButtonEnabled = False
holdAllButtonEnabled = False

def renderCard(position, card):

	suit = convertSuitToUnicode(card.suit)

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
	twoPair = myFont.render("Two Pairs: 25", 1, (255,255,0))
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
def renderPlayerScore():
	pygame.draw.rect(screen, colors['blue'], (575, 30, 175, 20))
	playerScoreText = myFont.render("Player Score: " + str(playerScore), 1, (255,255,0))
	screen.blit(playerScoreText, (575, 32))

def renderDrawNewHandButton():
	newHandButtonPos = (50, 400, 100, 25)
	newHandButtonText = buttonFont.render("Draw New Hand", 1, (0, 0, 0))
	if drawNewHandButtonEnabled == True:
		pygame.draw.rect(screen, colors['black'], (50, 400, 77, 27))
		pygame.draw.rect(screen, colors['white'], newHandButtonPos)
		screen.blit(newHandButtonText, (55, 407))
	else:
		pygame.draw.rect(screen, colors['black'], (50, 400, 77, 27))
		pygame.draw.rect(screen, colors['grey'], newHandButtonPos)
		screen.blit(newHandButtonText, (55, 407))

def renderDiscardButtons():
	
	discardButtonText = buttonFont.render("Discard", 1, (0, 0, 0))
	undiscardButtonText = buttonFont.render("Hold", 1, (0, 0, 0))
	buttonXPos =  65
	buttonYPos = 355

	for i in range(handSize):
		pygame.draw.rect(screen, colors['black'], (buttonXPos, 357, 72, 29))
		if playerHand.hand[i] in discards:
			pygame.draw.rect(screen, colors['white'], (buttonXPos, buttonYPos, 70, 27))
			screen.blit(undiscardButtonText, (buttonXPos + 20, 362))
		else:
			pygame.draw.rect(screen, colors['white'], (buttonXPos, buttonYPos, 70, 27))
			screen.blit(discardButtonText, (buttonXPos + 10, 362))
		buttonXPos += 150
		
def renderHoldAllButton():
	if holdAllButtonEnabled == True:
		holdAllButtonText = buttonFont.render("Hold All", 1, (0, 0, 0))
		pygame.draw.rect(screen, colors['black'], (245, 400, 77, 27))
		pygame.draw.rect(screen, colors['white'], (245, 400, 75, 25))
		screen.blit(holdAllButtonText, (255, 407))
	else:
		holdAllButtonText = buttonFont.render("Hold All", 1, (0, 0, 0))
		pygame.draw.rect(screen, colors['black'], (245, 400, 77, 27))
		pygame.draw.rect(screen, colors['grey'], (245, 400, 75, 25))
		screen.blit(holdAllButtonText, (255, 407))

def renderDiscardAllButton():
	if discardAllButtonEnabled == True:
		holdAllButtonText = buttonFont.render("Discard All", 1, (0, 0, 0))
		pygame.draw.rect(screen, colors['black'], (325, 400, 77, 27))
		pygame.draw.rect(screen, colors['white'], (325, 400, 75, 25))
		screen.blit(holdAllButtonText, (329, 407))
	else: 
		holdAllButtonText = buttonFont.render("Discard All", 1, (0, 0, 0))
		pygame.draw.rect(screen, colors['black'], (325, 400, 77, 27))
		pygame.draw.rect(screen, colors['grey'], (325, 400, 75, 25))
		screen.blit(holdAllButtonText, (329, 407))

def renderDrawButton():
	if drawButtonEnabled == True:
		drawButtonText = buttonFont.render("Draw", 1, (0, 0, 0))
		pygame.draw.rect(screen, colors['black'], (160, 400, 77, 27))
		pygame.draw.rect(screen, colors['white'], (160, 400, 75, 25))
		screen.blit(drawButtonText, (185, 407))
	else:
		drawButtonText = buttonFont.render("Draw", 1, (0, 0, 0))
		pygame.draw.rect(screen, colors['black'], (160, 400, 77, 27))
		pygame.draw.rect(screen, colors['grey'], (160, 400, 75, 25))
		screen.blit(drawButtonText, (185, 407))

def getMousePos():
	return pygame.mouse.get_pos()

def getClick():
	if pygame.mouse.get_pressed() == (1,0,0):
		print True
	else:
		return False

def renderHand():
	renderCard(card1, playerHand.hand[0])
	renderCard(card2, playerHand.hand[1])
	renderCard(card3, playerHand.hand[2])
	renderCard(card4, playerHand.hand[3])
	renderCard(card5, playerHand.hand[4])

renderScoreTable(scoreTable)
renderPlayerScore()

renderDrawNewHandButton()
renderHoldAllButton()
renderDrawButton()
renderDiscardAllButton()

newHandButtonRect = (50, 400, 100, 25)
drawButtonRect = (160, 400, 77, 27)
discardAllButtonRect = (325, 400, 75, 25)
holdAllButtonRect = (245, 400, 75, 25)

discardButtonRect1 = (75, 355, 50, 27)
discardButtonRect2 = (225, 355, 50, 27)
discardButtonRect3 = (375, 355, 50, 27)
discardButtonRect4 = (525, 355, 50, 27)
discardButtonRect5 = (675, 355, 50, 27)

holdButtonCordinates = {0:(75, 355), 1:(225, 355), 2:(375, 355), 3:(525, 355), 4:(675, 355)}



def isRectClicked(dimensions):
	mousePosition = pygame.mouse.get_pos()
	if mousePosition[0] > dimensions[0] and mousePosition[0] < dimensions[0] + dimensions[2]:
		if mousePosition[1] > dimensions[1] and mousePosition[1] < dimensions[1] + dimensions[3]:
			return True

def isDiscardButtonClicked():
	#card1
	if isRectClicked(discardButtonRect1) == True:
		return playerHand.hand[0]
	#card2
	if isRectClicked(discardButtonRect2) == True:
		return playerHand.hand[1]
	#card3
	if isRectClicked(discardButtonRect3) == True:
		return playerHand.hand[2]
	#card4
	if isRectClicked(discardButtonRect4) == True:
		return playerHand.hand[3]
	#card5
	if isRectClicked(discardButtonRect5) == True:
		return playerHand.hand[4]
	else:
		return False



while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:

			if isRectClicked(newHandButtonRect) == True: #Checks if 'New Hand' button is clicked
				deck = poker.newDeck()
				playerHand = poker.hand(poker.drawHand(deck))
				renderHand()
				discards = set()
				renderDiscardButtons()
				discardAllButtonEnabled = True
				renderDiscardAllButton()
				drawButtonEnabled = True
				renderDrawButton()
				drawNewHandButtonEnabled = False
				renderDrawNewHandButton()

			if isDiscardButtonClicked() != False:
				if isDiscardButtonClicked() not in discards:
					discards.add(isDiscardButtonClicked())
				else:
					discards.remove(isDiscardButtonClicked())
				renderDiscardButtons()
				print discards

			if isRectClicked(drawButtonRect) == True: #Checks is 'Draw' button is clicked
				if len(discards) > 0:
					playerHand.discard(discards, deck)
					discards = set()
				renderHand()
				playerHand.scoreHand()
				playerScore += playerHand.scoreHand()
				renderPlayerScore()
				drawButtonEnabled = False
				renderDrawButton()
				drawNewHandButtonEnabled = True
				renderDrawNewHandButton()

			if isRectClicked(discardAllButtonRect) == True:
				if discardAllButtonEnabled == True:
					for card in playerHand.hand:
						discards.add(card)
						discardAllButtonEnabled = False
						renderDiscardAllButton()
						holdAllButtonEnabled = True
						renderHoldAllButton()
					print discards
				else:
					print False

			if isRectClicked(holdAllButtonRect) == True:
				if holdAllButtonEnabled == True:
					discards = set()
					print discards
					holdAllButtonEnabled = False
					renderHoldAllButton()
					discardAllButtonEnabled = True
					renderDiscardAllButton()
				else:
					print False
			renderDiscardButtons()
		if event.type == QUIT:
			pygame.quit()
			sys.ext()
	pygame.display.update()
