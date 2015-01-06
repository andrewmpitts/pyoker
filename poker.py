#card logic
import random
import sys
import collections
import _abcoll


J = 11
Q = 12
K = 13
A = 14

handSize = 5

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

def drawHand(deck):
    hand = []
    for i in range(handSize):
        hand.append(deck.pop())
    return hand

def drawCard(deck):
    return deck.pop()

class hand(object):
    
    def __init__(self, hand):
        self.hand = hand
        self.length = len(hand)
        # self.cards = 

    def discard(self, discards, deck):
        if len(discards) > 0:
            for i in discards:
                self.hand.remove(i)
                self.hand.append(drawCard(deck))
            return self.hand
        else:
            return False

    # Designates cards to omit from draw
    def hold(self, cardsHeld):
        newHand = []
        for i in range(len(cardsHeld)):
            newHand.append(self.hand[i])
        for i in range(handSize - len(cardsHeld)):
            newHand.append(drawCard(deck))
        self.hand = newHand
        return newHand

    def scoreHand(self):
        
        if checkStraightFlush(self) == True:
            # print "Straight Flush: 175 Points"
            return 175

        if checkFourPair(self) == True:
            # print "Four of a Kind: 150 Points"
            return 150

        if checkFullHouse(self) == True:
            # print "Full House: 125 Points"
            return 125

        if checkFlush(self) == True:
            # print "Flush: 100 Points"
            return 100

        if checkStraight(self) == True:
            # print "Straight: 75 Points"
            return 75

        if checkThreePair(self) == True:
            # print "Three of a Kind: 50 Points"
            return 50

        if checkTwoPairs(self) == True:
            # print "Two Pairs: 25 Points"
            return 25

        if checkPair(self) == True:
            # print "Pair: 10 Points"
            return 10

        # print "No valid hands. You lose."
        return -25


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

    def sortHand(self):
        sortedHand = sorted(self.getRanks)
        self.hand == sortedHand

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

def checkStraightFlush(hand):
    if checkFlush(hand) == True and checkStraight(hand) == True:
        return True, checkHighCard(hand)

def checkFullHouse(hand):
    hand = sorted(hand.getRanks())
    if hand[2] == hand[4]:
        return True, hand[1], hand[2]
    if hand[0] == hand[2]:
        return True, hand[0], hand[3]
    else:
        return False

def checkTwoPairs(hand):
    ranks = sorted(hand.getRanks())
    pair = []
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
    for i in range(4):
        if ranks.count(ranks[i]) == 2:
            return True
    return False