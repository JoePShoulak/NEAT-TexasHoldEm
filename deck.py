from random import shuffle

from card import Card


class Deck:
    CARDS = []  # need to give it card objects

    def __init__(self):
        for suit in ['hearts', 'diamonds', 'spades', 'clubs']:
            for label, value in [["2", 2], ["3", 3], ["4", 4], ["5", 5], ["6", 6], ["7", 7], ["8", 8], ["9", 9],
                                 ["10", 10], ["J", 11], ["Q", 12], ["K", 13], ["A", 14]]:
                self.CARDS.append(Card(suit, value, label))
        shuffle(self.CARDS)

    def length(self):
        return len(self.CARDS)

    def deal(self, player):
        player.hand = self.CARDS[0:2]
        self.CARDS = self.CARDS[2:]

    def display(self):
        for card in self.CARDS:
            print("%s of %s" % (card.label, card.suit))
