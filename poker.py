#card logic
import random
import collections
from collections import Counter, namedtuple
from enum import Enum

Card = namedtuple('Card', ['rank', 'suit'])

class Score(Enum):
    NOTHING = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

class Suit(Enum):
    HEART = 'H'
    DIAMOND = 'D'
    CLUB = 'C'
    SPADE = 'S'

class Hand(object):
    
    def __init__(self, hand):
        self.cards = list(cards)

    def replace(self, discards, newcards):
        self.cards = [card for card in self.cards if card not in discards].extend(newcards)
        
    def scoreHand(self):
        sortedRanks = sorted([card.rank for card in self.cards])
        if sortedRanks == [2, 3, 4, 5, 14]:
            sortedRanks = [1, 2, 3, 4, 5]

        rankCounts = sorted(Counter(sranks).values())
        oneSuit = len(set([card.suit for card in self.cards])) == 1
        straight = len(rankCounts) == 5 and (sortedRanks[-1] - sortedRanks[0]) == 4

        result = Score.NOTHING

        if onesuit:
            if seq:
                if sortedRanks[-1] == 14:
                    result = Score.ROYAL_FLUSH
                else:
                    result = Score.STRAIGHT_FLUSH
            else:
                result = Score.FLUSH

        elif seq:
            result = Score.STRAIGHT
        elif rankCounts == [2, 3]:
            result = Score.FULL_HOUSE
        elif rankCounts == [1, 2, 2]:
            result = Score.TWO_PAIR
        elif 4 in rankCounts:
            result = Score.FOUR_KIND
        elif 3 in rankCounts:
            result = Score.THREE_KIND
        elif 2 in rankCounts:
            result = Score.PAIR

        return result

class Deck():
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Suit for rank in range(2, 15)]
        random.shuffle(self.cards)
 
    def draw(self, count):
        result = self.cards[-count:]
        self.cards = self.cards[:-count]
 
        return result