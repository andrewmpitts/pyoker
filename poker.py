#card logic
import random
import sys
import collections

class Card(object):

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

class Hand(object):
    
    def __init__(self, hand):
        self.hand = hand

    def discard(self, discards, deck):
        if len(discards) > 0:
            for i in discards:
                self.hand.remove(i)
                self.hand.append(drawCard(deck))
            return self.hand
        else:
            return False

    def scoreHand(self):
        
        if self.checkRoyalFlush() == True:
            print "Royal Flush: 200 Points"
            return 200

        if self.checkStraightFlush() == True:
            print "Straight Flush: 175 Points"
            return 175

        if self.checkFourPair() == True:
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

        if self.checkThreePair() == True:
            print "Three of a Kind: 50 Points"
            return 50

        if self.checkTwoPairs() == True:
            print "Two Pairs: 25 Points"
            return 25

        if self.checkPair() == True:
            print "Pair: 10 Points"
            return 10

        print "No valid hands. You lose."
        return -25


    def getCards(self):
        cards = []
        for i in range(len(self.hand)):
            cards.append(self.hand[i])
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

    def getHighCard(self):
        return max(self.getRanks())

    def checkFlush(self):
        return len(self.countSuitMatches()) == 1

    def checkStraight(self):
        hand = sorted(self.getRanks())
        if self.getRanks() == [2,3,4,5,14]:
            return True
        return hand[4] - 4 == hand[0] and len(self.countRankMatches()) == 5

    def checkStraightFlush(self):
        return self.checkFlush() == True and self.checkStraight() == True

    def checkRoyalFlush(self):
        if self.checkFlush() == True and self.checkStraight() == True:
            return sum(self.getRanks()) == 60

    def checkFullHouse(self):
        hand = sorted(self.getRanks())
        print self.getRanks()
        if len(self.countRankMatches()) == 2:
            return True
        else:
            return False

    def checkTwoPairs(self):
        ranks = sorted(self.getRanks())
        return ranks.count(ranks[1]) == 2 and ranks.count(ranks[3]) == 2

    def checkFourPair(self):
        ranks = sorted(self.getRanks())
        for i in range(2):
            if ranks.count(ranks[i]) == 4:
                return True
        else:
            return False

    def checkThreePair(self):
        ranks = sorted(self.getRanks())
        for i in range(3):
            if ranks.count(ranks[i]) == 3:
                return True
        return False

    def checkPair(self):
        ranks = sorted(self.getRanks())
        for i in range(4):
            if ranks.count(ranks[i]) == 2:
                return True
        return False

#Deck functions
def newDeck():
    newDeck = []
    for i in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
        for n in ['heart','diamond','club','spade']:
            newDeck.append(Card(i,n))
    random.shuffle(newDeck)
    return newDeck

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

