# This module is to be used with card games. It initialises a deck, with the ability
# to deal cards to specified hands. It was created as a way to introduce teens
# to the concepts of object-oriented programming using a language they are familiar
# with (as we have been learning it in class together). There are better languages
# for OOP, but using python in this context removes the need to learn new syntax
# as well as the theory.



import random

class Card(object):     #a class of card 'meanings'
    
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def str(self):
        if self.rank==11:
            value='Jack'
        elif self.rank==12:
            value='Queen'
        elif self.rank==13:
            value="King"
        elif self.rank==14:
            value="Ace"
        else:
            value=self.rank
        return str(value)+" of "+self.suit #print "Ace of Clubs" for 

    def isBetter(self, other):
        if self.rank == other.rank:
            return self.suit > other.suit
        else:
            return self.rank>other.rank
        #returns true if player's card is greater than the other card


class Deck(object):     #a class made of cards left to draw

#construct and populate the deck
    def __init__(self, ranks=None, suits=None): 
        self.deck=[]
        self.build()
        
    def build(self):
        for r in range(2, 15):
            for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
                self.deck.append(Card(r, s))
        
#deal a card out, and remove it from the deck
    def deal(self):
        if len(self.deck)<1:
            self.deck.build()
        x=random.randint(0, len(self.deck)-1)
        card=self.deck[x]
        del self.deck[x]            #remove the selected card from the deck
        return card                #return the selected cards 

class Hand(object):     #a class made of card the player has

#construct the hand
    def __init__(self, cards=None):
        self.hand=[]

#draw a card to the player's hand
    def draw(self,deck):
        self.hand.append(Deck.deal())   #add the cards you draw to the hand

# hint: you may need to add more functions to make other games work
        

