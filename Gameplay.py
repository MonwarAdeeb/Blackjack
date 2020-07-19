from Classes import Variables
from Classes import Card
from Classes import Deck
from Classes import Hand

test_deck = Deck.Deck()
test_deck.shuffle()

test_player = Hand.Hand()
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)

print(test_player.value)

test_player.add_card(test_deck.deal())
print(pulled_card)
print(test_player.value)