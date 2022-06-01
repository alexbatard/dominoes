import pygame
from .constants import SQUARE_SIZE, DOMINO_BACK


class HalfDomino:
    '''
    Allows the representation of each half-domino.
    '''

    def __init__(self, row, col, value, player):
        self.row = row
        self.col = col
        self.value = value
        self.player = player
        self.is_on_board = False
        self.neighbors = {}
        self.x = 0
        self.y = 0
        self.calcPos()

    def calcPos(self):
        '''
        Determines the coordinates of the half-domino.
        '''
        # give x and y position based on the current row and column
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def placeOnBoard(self):
        '''
        Updates the is_on_board variable when a half-domino is placed
        on the board.
        '''
        # change state of the half domino
        self.is_on_board = True

    def draw(self, win):
        '''
        Graphically represents a half-domino.
        It associates a pre-recorded image with each half-domino.
        '''
        DOMINO_IMAGE = pygame.transform.scale(
            pygame.image.load(f"assets/dom_{self.value}.png"), (40, 40))
        DOMINO_IMAGE_RECT = DOMINO_IMAGE.get_rect(center=(self.x, self.y))
        win.blit(DOMINO_IMAGE, DOMINO_IMAGE_RECT)

    def drawHidden(self, win):
        '''
        Graphically represents the back of a half-domino (hidden).
        It associates a pre-recorded image with each half-domino.
        '''
        DOMINO_BACK_RECT = DOMINO_BACK.get_rect(center=(self.x, self.y))
        win.blit(DOMINO_BACK, DOMINO_BACK_RECT)

    def fromHandToBoard(self, row, col):
        '''
        Called when a domino is placed on the board.
        '''
        self.row = row
        self.col = col
        self.calcPos()
        self.placeOnBoard()

    def getNeighborNumber(self):
        '''
        Returns the number of neighbors of the half-domino.
        '''
        return sum(self.neighbors.values())

    def __repr__(self):
        '''
        Representation of the half-domino (when printed).
        '''
        return str(self.value)
