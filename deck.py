from enum import Enum # Bound symbolic names to constant, uniqe values
from enum import IntEnum
from random import randint


class Card(IntEnum):
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Suit(Enum):
    SPADES = 'spades'  # Pik
    CLUBS = 'clubs'  # Trefl
    HEARTS = 'hearts'  # Serce, Kier
    DIAMONDS = 'diamonds'  # Karo


class PlayingCard:
    def __init__(self, card_value, card_suit):
        self.card = card_value
        self.suit = card_suit

    def __eq__(self, other):
        return self.card == other.card and self.suit == other.suit
    
    def __lt__(self, other):
        return self.card < other.card
    
    def print_card(self):
        print(self.card, self.suit, end=' ')


class Deck:
    def __init__(self):
        self.deck = []

    def create_stock_deck(self):
        for suit in Suit:
            for card in Card:
                self.deck.append(PlayingCard(Card(card), Suit(suit)))

    def print_deck(self):
        self.sort()
        for i in range(0, len(self.deck)):
            self.deck[i].print_card()
            print(i)
        print("Cards in self.deck: ", len(self.deck))
        print()

    def draw_card(self):
        rand_card = randint(0, len(self.deck) - 1)
        return self.deck.pop(rand_card)
    
    def push(self, card):
        self.deck.append(card)
    
    def pop(self):
        return self.deck.pop(len(self.deck) - 1)

    def pop_chosen_card(self, number):
        return self.deck.pop(number)

    def empty(self):
        if len(self.deck) == 0:
            return True
        return False

    def sort(self):
        self.deck = sorted(self.deck)

    def get_top_element(self):
        return self.deck[len(self.deck) - 1]

    def return_in_list(self):
        deck_list = []
        for i in range(len(self.deck)):
            deck_list.append(str(self.deck[i].card) + str(".") + str(self.deck[i].suit))
        return deck_list