#!/usr/bin/python


import sys


class Deck(object):
    cards = []

    def __init__(self):
        numbers = range(1, 11) + ['J', 'Q', 'K', 'A']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']

        self.cards = ["%s-%s" % (number, suit) for number in numbers for suit in suits]

    def __repr__(self):
        return "Standard Deck"

    def print_cards(self):
        for card in self.cards:
            sys.stdout.write(card + '\n')

    def faro_shuffle(self):
        """
        shuffles the deck using a perfect faro method
        """
        shuffled_deck = []

        first_split = self.cards[:len(self.cards) / 2]
        second_split = self.cards[len(self.cards) / 2:]

        for (a, b) in zip(first_split, second_split):
            shuffled_deck.append(a)
            shuffled_deck.append(b)

        self.cards = shuffled_deck

    def shuffle(self, times=777):
        for i in range(1, times):
            self.faro_shuffle()


def test():
    raw_input("Press any key to create a deck")

    sys.stdout.write("Creating deck instance...\n\n")
    deck = Deck()

    sys.stdout.write("Cards:\n")
    deck.print_cards()

    raw_input("\nPress any key to shuffle cards...\n")
    deck.shuffle()

    sys.stdout.write("Shuffled deck:\n")
    deck.print_cards()


if __name__ == "__main__":
    test()
