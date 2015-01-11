#card logic
import random
import collections

class Card(object):

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

class Hand(object):
    
    def __init__(self, hand):
        self.hand = hand

    def discard(self, discards, deck):
        newHand = []
        for card in range(5):
            if self.hand[card] not in discards:
                newHand.append(self.hand[card])
            else:
                newHand.append(drawCard(deck))
        self.hand = newHand
        return self.hand

    def scoreHand(self):
        
        if self.checkRoyalFlush() == True:
            print "Royal Flush: 200 Points"
            return 200

        if self.checkStraightFlush() == True:
            print "Straight Flush: 175 Points"
            return 175

        if self.checkFourKind() == True:
            print "Four of a Kind: 150 Points"
            return 150

        if self.checkFullHouse() == True:
            print "Full House: 125 Points"
            return 125

        if self.checkFlush() == True:
            print "Flush: 100 Points"
            return 100

        if self.checkStraight() == True:
            print "Straight: 75 Points"
            return 75

        if self.checkThreeKind() == True:
            print "Three of a Kind: 50 Points"
            return 50

        if self.checkTwoPair() == True:
            print "Two Pairs: 25 Points"
            return 25

        if self.checkPair() == True:
            print "Pair: 10 Points"
            return 10

        print "No valid hands. You lose."
        return -15


    def getRanks(self):
        return sorted([card.rank for card in self.hand])

    def getSuits(self):
        return [card.suit for card in self.hand]

    def countRankMatches(self):
        return collections.Counter(self.getRanks())

    def countSuitMatches(self):
        return collections.Counter(self.getSuits())

    def getHighCard(self):
        return max(self.getRanks())

    def checkFlush(self):
        return len(self.countSuitMatches()) == 1

    def checkStraight(self):
        orderedRanks = self.getRanks()
        if orderedRanks == [2,3,4,5,14]:
            return True
        return orderedRanks[4] - 4 == orderedRanks[0] and len(self.countRankMatches()) == 5

    def checkStraightFlush(self):
        return self.checkFlush() and self.checkStraight()

    def checkRoyalFlush(self):
        if self.checkFlush() and self.checkStraight():
            return sum(self.getRanks()) == 60

    def checkFullHouse(self):
        orderedRanks = self.getRanks()
        return orderedRanks.count(orderedRanks[0]) + orderedRanks.count(orderedRanks[4]) == 5

    def checkTwoPair(self):
        orderedRanks = self.getRanks()
        return orderedRanks.count(orderedRanks[1]) == 2 and orderedRanks.count(orderedRanks[3]) == 2

    def checkFourKind(self):
        orderedRanks = self.getRanks()
        for i in range(2):
            if orderedRanks.count(orderedRanks[i]) == 4:
                return True

    def checkThreeKind(self):
        orderedRanks = self.getRanks()
        for i in range(3):
            if orderedRanks.count(orderedRanks[i]) == 3:
                return True
        return False

    def checkPair(self):
        orderedRanks = self.getRanks()
        for i in range(4):
            if orderedRanks.count(orderedRanks[i]) == 2:
                return True
        return False

#Deck functions
def newDeck():
    newDeck = []
    for rank in range(2,15):
        for suit in ['heart','diamond','club','spade']:
            newDeck.append(Card(rank,suit))
    random.shuffle(newDeck)
    return newDeck

def recycleCards(discards):
    for cards in discards:
        deck.append(cards)

def shuffleDeck(deck):
    random.shuffle(deck)
    return deck

def drawHand(deck):
    hand = []
    for i in range(5):
        hand.append(deck.pop())
    return hand

def drawCard(deck):
    return deck.pop()

# Scoring

