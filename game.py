from deck import *
import json


class Player:
    def __init__(self, name):
        self.deck = Deck()
        self.player_move = False
        self.player_name = name


class Game:
    def __init__(self):
        self.main_deck = Deck()
        self.moves = 0
        self.numberOfPlayers = 2
        self.players = []
        self.end_of_game = False
        self.error_message = False

    def make_players(self):
        for i in range(0, self.numberOfPlayers):
            self.players.append(Player("Player {}".format(i+1)))

    def make_decks_for_players(self):
        self.main_deck.create_stock_deck()
        for i in range(0, int(len(self.main_deck.deck) / self.numberOfPlayers)):
            for player in self.players:
                player.deck.push(self.main_deck.draw_card())

    def add_to_deck_from_deck(self, deck_one, deck_two, number_of_card):
        deck_one.push(deck_two.pop_chosen_card(number_of_card))

    def start_game(self):
        self.make_decks_for_players()
        for player in self.players:
            if PlayingCard(Card(9), Suit('hearts')) in player.deck.deck:
                player.player_move = True
        # self.print_all_decks()
        self.error_message = False
        for player in self.players:
            player.deck.sort()

    def preparation(self):
        self.make_players()
        self.start_game()

    def check_possibility_of_move(self, card):
        if self.main_deck.empty():
            return True
        if self.main_deck.get_top_element() > card:
            return False
        else:
            return True

    def take_three_cards(self, deck):
        if len(self.main_deck.deck) > 3:
            for i in range(0, 3):
                self.add_to_deck_from_deck(deck, self.main_deck, (len(self.main_deck.deck) - 1))
        elif len(self.main_deck.deck) > 1:
            for i in range(1, len(self.main_deck.deck)):
                self.add_to_deck_from_deck(deck, self.main_deck, (len(self.main_deck.deck) - 1))

    def list_booleans_if_empty_deck(self):
        empty_decks = []
        for player in self.players:
            empty_decks.append(player.deck.empty())
        return empty_decks

    def change_players(self):
        if not self.error_message:
            if self.players[0].player_move:
                self.players[0].player_move = False
                self.players[1].player_move = True
            elif self.players[1].player_move:
                self.players[1].player_move = False
                self.players[0].player_move = True
        for player in self.players:
            player.deck.sort()

    def game_move(self, player, number):
        try:
            if number == 2137:
                if len(self.main_deck.deck) < 2:
                    self.error_message = True
                    return False
                self.take_three_cards(player.deck)
                return True
            if PlayingCard(Card(9), Suit('hearts')) in player.deck.deck:
                if player.deck.deck[number] == PlayingCard(Card(9), Suit('hearts')):
                    self.add_to_deck_from_deck(self.main_deck, player.deck, number)
                    return True
                else:
                    self.error_message = True
                    return False
            if self.check_possibility_of_move(player.deck.deck[number]):
                self.add_to_deck_from_deck(self.main_deck, player.deck, number)
                self.moves += 1
                return True
            else:
                self.error_message = True
                return False
        except IndexError:
            self.error_message = True
            return False

    def request_move(self, number):
        if not self.end_of_game:
            for i in range(0, len(self.players)):
                if self.players[i].player_move:
                    if self.game_move(self.players[i], number):
                        self.error_message = False
            if any(self.list_booleans_if_empty_deck()):
                self.end_of_game = True
            self.change_players()

    def print_all_decks(self):
        for player in self.players:
            if player.player_move:
                print(" ---------- {} DECK ---------- ".format(player.player_name))
                player.deck.print_deck()
        print(" ---------- MAIN DECK ----------")
        self.main_deck.print_deck()

    def reset(self):
        self.end_of_game = False
        self.main_deck.deck = []
        for player in self.players:
            player.player_move = False
            player.deck.deck = []
        self.start_game()



