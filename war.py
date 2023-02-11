#######################################
######### WELCOME TO WAR GAME #########
#######################################

# The deck is divided evenly, with each player receving 26 cards, dealt one at the time, face down. Anyone may deal 
# first. Each player places his stack of cards face down, in front of him.
#
# The play
#
# Each player turns up a card at the same time and the player with the higher card takes both cards and puts them,
# face down, on the bottom of his deck. 
#
# If the cards are the same rank, its is War. Each player turns up three cards face down and one card face up. If the 
# turned-up cards are again the same rank, each player places another card face down and turns up another card face
# up. The player with the higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now. 
# Ignore "double" wars.

from random import shuffle

# Two useful variables to create cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#mycards = [(s,r) for s in SUITE for r in RANKS]

'''
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))
'''

class Deck():

    """
    This is the Deck class. This object will create a deck of cards to initiate play. You can use this Deck list of cards 
    to split in half and give the players. It will SUITE and Ranks to create the deck. It should also have a method for 
    splitting/cutting the deck in half and shuffling the deck.
    """

    def __init__(self) -> None:
        print("Creating new ordered deck!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26], self.allcards[26:])

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add and remove cards from that Hand. There is should be an
    add and a remove method here.
    '''

    def __init__(self, cards) -> None:
        self.cards = cards

    def __str__(self) -> str:
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player():

    '''
    This is the Player class, which takes in a name and and instance of a Hand class Object.
    The player can play cards and check if they still have cards.
    '''
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
        return war_cards
        
    def still_has_cards(self):
        '''
        Return True if player still has cards left
        '''
        return len(self.hand.cards) != 0



##################################################
############## GAMEPLAY ##########################
##################################################

print("Welcome to the War game, let's begin ...")

# Create a new deck and split it in half
d = Deck()
d.shuffle()
half1,half2=d.split_in_half()

# create both players
comp = Player("computer",Hand(half1))
name = input("What's your name?")
user = Player(name, Hand(half2))

total_rounds  = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += total_rounds
    print("Time for a new round")
    print("Here are the current standings")
    print(user.name + "has the count: " + str(len(user.hand.cards)))
    print(comp.name + "has the count: " + str(len(comp.hand.cards)))
    print("play a card!")
    print("\n")

    table_cards = []
    c_card = comp.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("war!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
        
print("Game over, number of rounds: " + str(total_rounds))

print("A war happened: " + str(war_count) + " times")


