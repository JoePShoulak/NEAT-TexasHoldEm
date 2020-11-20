from deck import Deck
from player import Player

def main():
    deck = Deck()
    # deck.display()

    startingAmount = 100

    p1 = Player(startingAmount)
    p2 = Player(startingAmount)

    print("Deck length: %d" % deck.length())

    deck.deal(p1)
    deck.deal(p2)

    print("Deck length: %d" % deck.length())

    p1.displayHand()
    p2.displayHand()


if __name__ == "__main__":
    main()
