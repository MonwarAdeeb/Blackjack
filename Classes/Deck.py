from Classes import Variables
from Classes import Card

class Deck():

    def __init__(self):
        self.deck = []

        for suit in Variables.suits:
            for rank in Variables.ranks:
                self.deck.append(Card.Card(suit,rank))



    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' +card.__str__()

        return "The deck has: " + deck_comp

    # Suffles the deck
    def shuffle(self):
        Variables.random.shuffle(self.deck)

    # Deals a single card
    def deal(self):
        single_card = self.deck.pop()
        return single_card