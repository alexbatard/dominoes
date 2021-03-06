from random import randint
import pygame
# relative imports
from .constants import LIGHT_CYAN, PALE_TURQUOISE, TEAL, ROWS, COLS,\
    SQUARE_SIZE, PLAYER1, PLAYER2
from .half_domino import HalfDomino


class Board(list):
    '''
    The Board class represents the game board.
    It takes care of all the movements of the pieces,
    their creation and deletion, as well as drawing of
    the board on the screen.
    '''
    # internal representation of the board: 2D list
    def __init__(self, dominoes_per_player=7):
        assert dominoes_per_player <= 14
        self.dominoes_per_player = dominoes_per_player
        self.domino_values = []  # list of tuples ex: (5, 3),
        # representing domino values. It is the stock of the game

        # store the dominoes per player, represented by tuples
        self.player1_dominoes = []
        self.player2_dominoes = []
        self.player3_dominoes = []
        self.player4_dominoes = []

        self.createBoard()  # when the object is created,
        # the board is automatically created

    def drawBackground(self, win):
        '''
        Draws the background of the game board (graphic representation).
        '''
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

    def fillDominoValues(self):
        '''
        Creates the internal representations of the dominoes
        (tuples of 2 values).
        Used to fill the domino_values variable with all the
        possible dominoes (28).
        '''
        # represents the stock at the beginning of the game
        for i in range(7):
            for j in range(7):
                if (i, j) not in self.domino_values:
                    if (j, i) not in self.domino_values:  # no doubles
                        self.domino_values.append((i, j))

    def fromStockToHand(self, row, col, player):
        '''
        Complements the create_board method.
        Selects a random pair of values from the deck and adds
        these two half-dominoes to the list that makes up the player's hand.
        '''
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
        piece_1 = HalfDomino(row, col, domino_value[0],
                             player)  # create domino
        piece_2 = HalfDomino(row + 1, col, domino_value[1], player)
        self[row].append(piece_1)
        if col == 0:
            self.append([])
        self[row + 1].append(piece_2)
        self.domino_values.remove(domino_value)
        return domino_value

    def pickPiece(self, row, col, player):
        '''
        Picks a piece from the stock if a player can't play.
        '''
        domino_value = self.domino_values[randint(0,
                                                  len(self.domino_values) -
                                                  1)]  # random domino value
        piece_1 = HalfDomino(row, col, domino_value[0],
                             player)  # create domino
        piece_2 = HalfDomino(row + 1, col, domino_value[1], player)
        self[row][col] = piece_1
        self[row + 1][col] = piece_2
        self.domino_values.remove(domino_value)
        return domino_value

    def createBoard(self):
        '''
        Creates the internal representation of the board (2-dimensional list).
        It randomly assigns the dominoes to the players and initializes
        the squares of the game area with "x".
        '''
        # represents the game setup: dealing dominoes to the players
        self.fillDominoValues()
        for row in range(ROWS):
            # rows 1 & 15 will be added when putting
            # the 1st domino on rows 0 & 14
            if row != 1 and row != ROWS - 1:
                self.append([])  # 1 list represents a row
            for col in range(COLS):
                if col < self.dominoes_per_player:
                    if row == 0:
                        domino_value = self.fromStockToHand(row, col, PLAYER2)
                        self.player2_dominoes.append(domino_value)
                    elif row == ROWS - 2:
                        domino_value = self.fromStockToHand(row, col, PLAYER1)
                        self.player1_dominoes.append(domino_value)
                    elif row != 1 and row != ROWS - 1:
                        self[row].append('x')
                else:
                    self[row].append('x')

    def draw(self, win, player):
        '''
        Graphically represents the background and the pieces.
        '''
        # draw the background and the dominoes in the window (GUI)
        self.drawBackground(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self[row][col]
                if piece != 'x':
                    if player == PLAYER1:
                        if piece.player == PLAYER1 or \
                         piece.is_on_board:
                            piece.draw(win)
                        else:
                            piece.drawHidden(win)
                    elif player == PLAYER2:
                        if piece.player == PLAYER2 or \
                         piece.is_on_board:
                            piece.draw(win)
                        else:
                            piece.drawHidden(win)
                    else:
                        if piece.is_on_board:
                            piece.draw(win)
                        else:
                            piece.drawHidden(win)

    def fromHandToBoard(self, piece, row, col):
        '''
        Allows moving a half-domino on the board.
        '''
        self[piece.row][piece.col], self[row][col] = self[row][col], self[
            piece.row][piece.col]
        piece.fromHandToBoard(row, col)

    def getPiece(self, row, col):
        '''
        Returns the piece at the given row and column on the board.
        '''
        return self[row][col]

    def getNeighbors(self, piece):
        '''
        Allows the modification of the instance variable piece.neighbors,
        a dictionary associating to each direction (top, bottom, left, right)
        0 if there is no domino on the neighbouring square
        in this direction, and 1 if there is one.
        '''
        neighbors = {'top': 0, 'bottom': 0, 'left': 0, 'right': 0}
        if self.getPiece(piece.row - 1, piece.col) != 'x':
            neighbors['top'] = 1
        if self.getPiece(piece.row + 1, piece.col) != 'x':
            neighbors['bottom'] = 1
        if self.getPiece(piece.row, piece.col - 1) != 'x':
            neighbors['left'] = 1
        if self.getPiece(piece.row, piece.col + 1) != 'x':
            neighbors['right'] = 1
        piece.neighbors = neighbors
