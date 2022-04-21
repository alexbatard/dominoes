from random import randint
from .constants import CRIMSON_RED, ROWS, COLS  # relative import
from .domino import Domino


class Board:

    def __init__(self, nb_players, nb_dominoes_per_player):
        assert nb_players == 2 or nb_players == 3 \
            or nb_players == 4
        assert nb_players * nb_dominoes_per_player <= 28
        self.board = []  # internal representation of the board: 2D list
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
        self.create_board()

    def draw_background(self, win):
        # draw the background of the board in the window (GUI)
        win.fill(CRIMSON_RED)

    def fill_domino_values(self):
        # fills the domino_values variable with all the values
        # possible for dominoes
        # (represents the stock at the beginning of the game)
        for i in range(7):
            for j in range(7):
                if (i, j) not in self.domino_values:
                    if (j, i) not in self.domino_values:  # no doubles
                        self.domino_values.append((i, j))

    def from_stock_to_hand(self, i, row, col):
        # select a random domino value from stock
        # create the corresponding domino
        # add it to the internal representation of the board,
        # in the player's hand (vertically)
        # remove the domino value from stock
        # set the domino as not in stock
        # and return the value for it to be reused
        domino_value = self.domino_values[randint(0, i)]  # random domino value
        domino = Domino(row, col, row + 1, col, domino_value)  # create domino
        self.board[row].append(domino)
        self.board.append([])
        self.board[row + 1].append(domino)
        self.domino_values.remove(domino_value)
        domino.draw_from_stock()
        return domino_value

    def create_board(self):
        # create internal representation of the board
        # at the beginning of the game
        # represents the game setup: dealing dominoes to the players
        self.fill_domino_values()
        i = 27  # counts the number of dominoes drawn, decreasing from 27
        # and makes sure the right number of dominoes is drawn
        while i > 27 - self.nb_players * self.nb_dominoes_per_player:
            for row in range(ROWS):
                # rows 1 & 15 will be added when putting
                # the 1st domino on rows 0 & 14
                if row != 1 and row != 15:
                    self.board.append([])  # 1 list per row
                for col in range(COLS):
                    if col < self.nb_dominoes_per_player:
                        if row == 0:
                            domino_value = self.from_stock_to_hand(i, row, col)
                            self.player2_dominoes.append(domino_value)
                            i -= 1
                        elif row == 14:
                            domino_value = self.from_stock_to_hand(i, row, col)
                            self.player1_dominoes.append(domino_value)
                            i -= 1
                        elif row != 1 and row != 15:
                            self.board[row].append(0)
                    else:
                        if row != 1 and row != 15:
                            self.board[row].append(0)

    def draw(self, win):
        # draw the background and the dominoes in the window (GUI)
        self.draw_background(win)
        for row in range(ROWS):
            for col in range(COLS):
                domino = self.board[row][col]
                if domino != 0 and row != 1 and row != 15:
                    domino.draw(win)
