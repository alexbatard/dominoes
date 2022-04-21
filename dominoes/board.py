# import pygame
from random import randint
from .constants import CRIMSON_RED, ROWS, COLS
from .domino import Domino


class Board:

    def __init__(self, nb_players, nb_dominoes_per_player):
        assert nb_players == 2 or nb_players == 3 \
            or nb_players == 4
        assert nb_players * nb_dominoes_per_player <= 28
        self.board = []  # internal representation of the board: 2D list

        # example with a 5x3 board:
        # [[-, 6, -, 3, -],
        #  [-, 3, -, 5, -],
        #  [-, 3, 4, 5, 1]]

        self.nb_players = nb_players
        self.nb_dominoes_per_player = nb_dominoes_per_player
        self.domino_values = []  # list of tuples ex: (5, 3),
        # representing domino values

        self.player1_dominoes = self.player2_dominoes = self.player3_dominoes \
            = self.player4_dominoes = []  # store the dominoes per player,
        # represented by tuples like in domino_values
# when the player puts a domino on the board, remove the  domino from the list
# when he draws a domino from the stock, add it to the list
# the list gives access to the number of dominoes left per player (using len())

    def draw_board(self, win):
        win.fill(CRIMSON_RED)

    def fill_domino_values(self):
        for i in range(7):
            for j in range(7):
                if (i, j) not in self.domino_values:
                    if (j, i) not in self.domino_values:  # no doubles
                        self.domino_values.append((i, j))

    def from_stock_to_hand(self, i, row, col):
        domino_value = self.domino_values[randint(0, i)]  # random domino value
        domino = Domino(row, col, row + 1, col, domino_value)  # create domino
        self.board[row].append(domino)
        self.board.append([])
        self.board[row + 1].append(domino)
        self.domino_values.remove(domino_value)
        domino.draw_from_stock()
        return domino_value

    # function designed for 2 players first
    def create_board(self):
        Board.fill_domino_values()
        i = 27  # counts the number of dominoes drawn, decreasing from 27
        while i > 27 - self.nb_players * self.nb_dominoes_per_player:
            for row in range(ROWS):
                if row != 1 and row != 15:
                    self.board.append([])
                for col in range(COLS):
                    if col < self.nb_dominoes_per_player:
                        if row == 0:
                            domino_value = self.from_stock_to_hand(i, row, col)
                            self.player2_dominoes.append(domino_value)
                            i -= 1
                        if row == 14:
                            domino_value = self.from_stock_to_hand(i, row, col)
                            self.player1_dominoes.append(domino_value)
                            i -= 1
