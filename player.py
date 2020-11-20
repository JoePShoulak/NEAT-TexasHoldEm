class Player:
    bet = 0
    hand = []
    isPlaying = True

    def __init__(self, money):
        self.money = money

    def meetAction(self, amount):
        self.bet += amount
        self.money -= amount

    def fold(self):
        self.isPlaying = False

    def displayHand(self):
        for card in self.hand:
            print("%s of %s" % (card.label, card.suit))
