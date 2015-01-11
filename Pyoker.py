# Pyoker
import pygame
import sys
import poker
# import pyokergraphics
from pygame.locals import *

X_RES = 800
Y_RES = 450

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((X_RES, Y_RES))
pygame.display.set_caption("Video Pyoker")
screen.fill((0,0,255))
clock = pygame.time.Clock()

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
CARD_WIDTH = 100
CARD_HEIGHT = 150
cardPositions = [(50, 200, CARD_WIDTH, CARD_HEIGHT), (200, 200, CARD_WIDTH, CARD_HEIGHT), (350, 200, CARD_WIDTH, CARD_HEIGHT), (500, 200, CARD_WIDTH, CARD_HEIGHT), (650, 200, CARD_WIDTH, CARD_HEIGHT)]


DISCARD_BUTTON_WIDTH = 50
DISCARD_BUTTON_HEIGHT = 27
DISCARD_BUTTON_SHADOW_WIDTH = 52
DISCARD_BUTTON_SHADOW_HEIGHT = 29
discardButtonPositions = [(75, 355, DISCARD_BUTTON_WIDTH, DISCARD_BUTTON_HEIGHT), (225, 355, DISCARD_BUTTON_WIDTH, DISCARD_BUTTON_HEIGHT), (375, 355, DISCARD_BUTTON_WIDTH, DISCARD_BUTTON_HEIGHT), (525, 355, DISCARD_BUTTON_WIDTH, DISCARD_BUTTON_HEIGHT), (675, 355, DISCARD_BUTTON_WIDTH, DISCARD_BUTTON_HEIGHT)]
discardButtonShadowPositions = [(75, 355, DISCARD_BUTTON_SHADOW_WIDTH, DISCARD_BUTTON_SHADOW_HEIGHT), (225, 355, DISCARD_BUTTON_SHADOW_WIDTH, DISCARD_BUTTON_SHADOW_HEIGHT), (375, 355, DISCARD_BUTTON_SHADOW_WIDTH, DISCARD_BUTTON_SHADOW_HEIGHT), (525, 355, DISCARD_BUTTON_SHADOW_WIDTH, DISCARD_BUTTON_SHADOW_HEIGHT), (675, 355, DISCARD_BUTTON_SHADOW_WIDTH, DISCARD_BUTTON_SHADOW_HEIGHT)]

newHandButtonRect = (50, 400, 100, 25)
drawButtonRect = (160, 400, 77, 27)
discardAllButtonRect = (325, 400, 75, 25)
holdAllButtonRect = (245, 400, 75, 25)

deck = poker.newDeck()
playerHand = poker.Hand(poker.drawHand(deck))
discards = set()

drawNewHandButtonEnabled = True
holdButtonsEnabled = False
drawButtonEnabled = False
discardAllButtonEnabled = False
holdAllButtonEnabled = False

def convertSuitToUnicode(suit): #Converts the card suit into Unicode for display in GUI
    if suit == 'spade':
        return spade
    if suit == 'club':
        return club
    if suit == 'diamond':
        return diamond
    else:
        return heart

def convertFaceCardRanks(card):

    if card.rank == 11:
        return "J"
    if card.rank == 12:
        return "Q"
    if card.rank == 13:
        return "K"
    if card.rank == 14:
        return "A"

# print convertFaceCardRanks(playerHand.hand[0])

def renderCard(position, card):

    suit = convertSuitToUnicode(card.suit)
    if card.rank > 10:
        rank = convertFaceCardRanks(card)
    else:
        rank = card.rank
    #draw card border
    pygame.draw.rect(screen, colors['black'], position)

    #draw card interior
    position = (position[0] + 2 ,position[1] + 2, 96, 146)
    pygame.draw.rect(screen, colors['white'], position)

    #render card rank
    rank = myFont.render(str(rank), 1, (0, 0, 0))
    screen.blit(rank, (position[0] + 10, position[1] + 5))
    screen.blit(rank, (position[0] + 75, position[1] + 125))

    #render card suit
    if suit == spade or suit == club:
        suit = suitFont.render(suit, 1, (0, 0, 0))
    else:
        suit = suitFont.render(suit, 1, (255, 0, 0))
    screen.blit(suit, (position[0] + 40, position[1] + 60))


def renderScoreTable():
    scoreTablePosition = (25, 25, 750, 150)
    #draw border
    pygame.draw.rect(screen, colors['white'], scoreTablePosition)
    
    #draw window
    scoreTableSInternalPosition = (scoreTablePosition[0] + 5 ,scoreTablePosition[1] + 5, 740, 140)
    pygame.draw.rect(screen, colors['blue'], scoreTableSInternalPosition)

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
    # scoredHand = myFont.render("Current Hand's Score: ", 1, (255,255,0))

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
    # screen.blit(scoredHand, (412, 45))

    #player score
def renderPlayerScore():
    pygame.draw.rect(screen, colors['blue'], (500, 30, 190, 20))
    playerScoreText = myFont.render("Player Score: " + str(playerScore), 1, (255,255,0))
    screen.blit(playerScoreText, (500, 32))

def renderDrawNewHandButton():
    newHandButtonPos = (50, 400, 100, 25)
    newHandButtonText = buttonFont.render("Draw New Hand", 1, (0, 0, 0))
    if drawNewHandButtonEnabled:
        pygame.draw.rect(screen, colors['black'], (50, 400, 102, 27))
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
        pygame.draw.rect(screen, colors['black'], discardButtonShadowPositions[i])
        if playerHand.hand[i] in discards:
            pygame.draw.rect(screen, colors['white'], discardButtonPositions[i])
            screen.blit(undiscardButtonText, (buttonXPos + 20, 362))
        else:
            pygame.draw.rect(screen, colors['white'], discardButtonPositions[i])
            screen.blit(discardButtonText, (buttonXPos + 10, 362))
        buttonXPos += 150
        
def renderHoldAllButton():
    if holdAllButtonEnabled:
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
    if discardAllButtonEnabled:
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
    if drawButtonEnabled:
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
    for i in range(handSize):
        renderCard(cardPositions[i], playerHand.hand[i])

renderScoreTable()
renderPlayerScore()
renderDrawNewHandButton()
renderHoldAllButton()
renderDrawButton()
renderDiscardAllButton()

def isRectClicked(dimensions):
    mousePosition = pygame.mouse.get_pos()
    if mousePosition[0] > dimensions[0] and mousePosition[0] < dimensions[0] + dimensions[2]:
        if mousePosition[1] > dimensions[1] and mousePosition[1] < dimensions[1] + dimensions[3]:
            return True

def isDiscardButtonClicked():
    for i in range(len(discardButtonPositions)):
        if isRectClicked(discardButtonPositions[i]):
            return playerHand.hand[i]
    return False

while True:
    for event in pygame.event.get():
        clock.tick(20)
        if event.type == pygame.MOUSEBUTTONUP: 
            if isRectClicked(newHandButtonRect):
                deck = poker.newDeck()
                playerHand = poker.Hand(poker.drawHand(deck))
                renderHand()
                discards = set()
                renderDiscardButtons()
                discardAllButtonEnabled = True
                renderDiscardAllButton()
                drawButtonEnabled = True
                renderDrawButton()
                drawNewHandButtonEnabled = False
                renderDrawNewHandButton()

            if isDiscardButtonClicked():
                if isDiscardButtonClicked() not in discards:
                    discards.add(isDiscardButtonClicked())
                else:
                    discards.remove(isDiscardButtonClicked())
                renderDiscardButtons()

            if isRectClicked(drawButtonRect): #Checks is 'Draw' button is clicked
                if len(discards) > 0:
                    playerHand.discard(discards, deck)
                    discards = set()
                renderHand()
                playerScore += playerHand.scoreHand()
                renderPlayerScore()
                drawButtonEnabled = False
                renderDrawButton()
                drawNewHandButtonEnabled = True
                renderDrawNewHandButton()
                discardAllButtonEnabled = False
                renderDiscardAllButton()
                holdAllButtonEnabled = False
                renderHoldAllButton()

            if isRectClicked(discardAllButtonRect):
                if discardAllButtonEnabled:
                    for card in playerHand.hand:
                        discards.add(card)
                        discardAllButtonEnabled = False
                        renderDiscardAllButton()
                        holdAllButtonEnabled = True
                        renderHoldAllButton()

            if isRectClicked(holdAllButtonRect):
                if holdAllButtonEnabled:
                    discards = set()
                    holdAllButtonEnabled = False
                    renderHoldAllButton()
                    discardAllButtonEnabled = True
                    renderDiscardAllButton()

            renderDiscardButtons()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
