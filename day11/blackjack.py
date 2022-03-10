from operator import indexOf
import random

#capstone

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
             'Queen':12, 'King':13, 'Ace':14}

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# deck is infinite, so cards can't be counted
# there are no jokers
# jack king queen all count as ten
# the will count as 11 until we go over 21
# cards are not removed from the deck

def game_start():

    f = open('day11/blackjack.txt')
    print(''.join([line for line in f]))
    print("\n")

    player_hand = []
    dealer_hand = []

    player_busted = False
    dealer_busted = False

    for num in range(0, 2):
        player_hand.append(cards[random.randint(0, len(cards) - 1)])
        dealer_hand.append(cards[random.randint(0, len(cards) - 1)])

    # Test hands
    # player_hand = [11, 5]
    # dealer_hand = [6, 7]

    player_new_card = 'y'

    while player_new_card == 'y':
        if sum(player_hand) <= 21:
            print("Player's hand is", player_hand, "->", sum(player_hand))
            print("Dealer's hand is", dealer_hand, "->", sum(dealer_hand))
            player_new_card = input("Type 'y' and press enter for a new card, or 'n' to stay: \n")
            if player_new_card == 'y':
                player_hand.append(cards[random.randint(0, len(cards) - 1)])
        else:
            if 11 in player_hand:
                print("Player's hand is", player_hand)
                print("Handling aces.....")
                player_hand = handle_aces(player_hand)
                print("Player's hand is", player_hand, "->", sum(player_hand))
                print("Dealer's hand is", dealer_hand, "->", sum(dealer_hand))
                player_new_card = input("Type 'y' and press enter for a new card, or 'n' to stay: \n")
                if player_new_card == 'y':
                 player_hand.append(cards[random.randint(0, len(cards) - 1)])
            else:
                print("\n")
                print("Busted!~!!!!!!!!!!")
                print("Player's hand is", player_hand, "->", sum(player_hand))
                print("Dealer's hand is", dealer_hand, "->", sum(dealer_hand))
                player_busted = True
                player_new_card = 'n'
            
    print("\n")
    print("Dealer turn")

    if player_busted == False:

        if sum(dealer_hand) < 17:
            dealer_new_card = 'y'
        else:
            dealer_new_card = 'n'

        while dealer_new_card == 'y':
            if sum(dealer_hand) <= 21:
                dealer_hand.append(cards[random.randint(0, len(cards) - 1)])
                print("Player's hand is", player_hand, "->", sum(player_hand))
                print("Dealer's hand is", dealer_hand, "->", sum(dealer_hand))
            else:
                dealer_new_card = 'n'

    print('\n')
    print('-----------------------------------------------------------------------')
    print("Player's hand is", player_hand, "->", sum(player_hand))
    print("Dealer's hand is", dealer_hand, "->", sum(dealer_hand))
        
def handle_aces(player_hand):

    new_hand = player_hand
    
    while sum(new_hand) > 21:
        new_hand[new_hand.index(11)] = 1
    
    print(new_hand)
    return new_hand


game_start()