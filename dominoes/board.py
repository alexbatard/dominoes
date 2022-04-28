from random import randint
import pygame
# relative imports
from .constants import LIGHT_CYAN, PALE_TURQUOISE, TEAL, ROWS, COLS,\
    SQUARE_SIZE
from .half_domino import HalfDomino


class Board:

    def __init__(self, nb_players, nb_dominoes_per_player):
        assert nb_players == 2 or nb_players == 3 \
            or nb_players == 4
        assert nb_players * nb_dominoes_per_player <= 28
        self.board = []  # internal representation of the board: 2D list
        self.nb_players = nb_players
        self.nb_dominoes_per_player = nb_dominoes_per_player
        self.domino_values = []  # list of tuples ex: (5, 3),
        # representing domino values. It is the stock of the game

        # store the dominoes per player, represented by tuples
        self.player1_dominoes = []
        self.player2_dominoes = []
        self.player3_dominoes = []
        self.player4_dominoes = []

        # when the player puts a domino on the board,
        # remove the  domino from the list
        # when he draws a domino from the stock, add it to the list
        # the list gives access to the number of dominoes
        # left per player (using len())

        self.create_board()  # when the object is created,
        # the board is automatically created

    def draw_background(self, win):
        # draw the background of the board in the window (GUI)
        win.fill(LIGHT_CYAN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, PALE_TURQUOISE,
                                 (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))
            if 0 <= row <= 2 or ROWS - 3 <= row <= ROWS - 1:
                for col in range(COLS):
                    pygame.draw.rect(win, TEAL,
                                     (col * SQUARE_SIZE, row * SQUARE_SIZE,
                                      SQUARE_SIZE, SQUARE_SIZE))

    def fill_domino_values(self):
        # fills the domino_values variable with all the values
        # possible for dominoes
        # (represents the stock at the beginning of the game)
        for i in range(7):
            for j in range(7):
                if (i, j) not in self.domino_values:
                    if (j, i) not in self.domino_values:  # no doubles
                        self.domino_values.append((i, j))

    def from_stock_to_hand(self, row, col):
        # select a random domino value from stock
        # create the 2 corresponding half dominoes
        # add them to the internal representation of the board,
        # in the player's hand (vertically)
        # remove the domino value from stock
        # set the half dominoes as not in stock
        # and return the value for it to be reused
        domino_value = self.domino_values[randint(0,
                                                  len(self.domino_values) -
                                                  1)]  # random domino value
        half_domino_1 = HalfDomino(row, col, domino_value[0])  # create domino
        half_domino_2 = HalfDomino(row + 1, col, domino_value[1])
        self.board[row].append(half_domino_1)
        if col == 0:
            self.board.append([])
        self.board[row + 1].append(half_domino_2)
        self.domino_values.remove(domino_value)
        half_domino_1.draw_from_stock()
        half_domino_2.draw_from_stock()
        return domino_value

    def create_board(self):
        # create internal representation of the board
        # at the beginning of the game
        # represents the game setup: dealing dominoes to the players
        self.fill_domino_values()
        for row in range(ROWS):
            # rows 1 & 15 will be added when putting
            # the 1st domino on rows 0 & 14
            if row != 1 and row != ROWS - 1:
                self.board.append([])  # 1 list per row
            for col in range(COLS):
                if col < self.nb_dominoes_per_player:
                    if row == 0:
                        domino_value = self.from_stock_to_hand(row, col)
                        self.player2_dominoes.append(domino_value)
                    elif row == ROWS - 2:
                        domino_value = self.from_stock_to_hand(row, col)
                        self.player1_dominoes.append(domino_value)
                    elif row != 1 and row != ROWS - 1:
                        self.board[row].append('x')
                else:
                    self.board[row].append('x')
        print(self.board)

    def draw(self, win):
        # draw the background and the dominoes in the window (GUI)
        self.draw_background(win)
        for row in range(ROWS):
            for col in range(COLS):
                half_domino = self.board[row][col]
                if half_domino != 'x':
                    if 0 <= row <= 1:
                        half_domino.draw_opponent(win)
                    else:
                        half_domino.draw_current_player(win)
