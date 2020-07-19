from Classes import Variables
from Classes import Card
from Classes import Deck

class Hand():

    def __init__(self):
        self.cards = []     # start with an empty list
        self.value = 0      # start with zero value
        self.aces = 0       # add an attribute to keep track of aces


    def add_card(self, card):
        # card passed in from Deck.deal() --> single_card(suit, rank)
        self.cards.append(card)
        self.value += Variables.values[card.rank]

        if card.rank == "Ace":
            self.aces += 1


    def adjust_for_aces(self):

        # if total value > 21 and I still have an Ace
        # Then change my Ace to be a 1 insteat of an 11
        # Here, selc.aces == selc.aces > 0, treating it as a boolean
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1