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
        for card in discards:
            self.hand.remove(card)
            self.hand.append(drawCard(deck))
        return self.hand

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
        return -15


    def getRanks(self):
        return sorted([card.rank for card in self.hand])

    def getSuits(self):
        return [card.suit for card in self.hand]

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
        return self.checkFlush() and self.checkStraight()

    def checkRoyalFlush(self):
        if self.checkFlush() and self.checkStraight():
            return sum(self.getRanks()) == 60

    def checkFullHouse(self):
        hand = sorted(self.getRanks())
        return hand.count(hand[0]) + hand.count(hand[4]) == 5

    def checkTwoPairs(self):
        ranks = sorted(self.getRanks())
        return ranks.count(ranks[1]) == 2 and ranks.count(ranks[3]) == 2

    def checkFourPair(self):
        ranks = sorted(self.getRanks())
        for i in range(2):
            if ranks.count(ranks[i]) == 4:
                return True

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

