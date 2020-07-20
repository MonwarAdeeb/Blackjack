from Classes import Variables
from Classes import Card
from Classes import Deck
from Classes import Hand
from Classes import Chips


# Taking bets
def take_bet(chips):

        while True:

            try:
                chips.bet = int(input("How many chips whould you like to bet? "))
            except:
                print("Sorry! Please provide an integer.")
            else:
                if chips.bet > chips.total:
                    print("Sorry, you do not have enough chips! You have {}".format(chips.total))
                else:
                    break

# Hitting cards
def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()


# Choice for hit or stand
def hit_or_stand(deck, hand):

    while True:
        x = input("Hit or Stand? Enter H or S : ")

        if x[0].lower() == 'h' :
            hit(deck, hand)

        elif x[0] == 's' :
            print("Player Stands, Dealer's Turn")
            Variables.playing = False
        
        else:
            print("Sorry, I didn't understand that. Please enter h or s only : ")
            continue
        
        break



# Show cards
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)



# Winning or losing scenarios
def player_busts(player, dealer, chips):
    print("Bust Player")
    chips.lost_bet()


def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player Wins! DEALER BUSTED!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lost_bet()

def push(player, dealer):
    print("Dealer and Player Tie! PUSH")





##########################
#    Gameplay Begin      #
##########################



while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck.Deck()
    deck.shuffle()
    
    player_hand = Hand.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips.Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while Variables.playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's total chips are at ",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' : ")
    
    if new_game[0].lower()=='y':
        Variables.playing=True
        continue
    else:
        print("Thanks for playing!")
        break