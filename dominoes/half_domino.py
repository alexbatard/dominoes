import pygame
from .constants import SQUARE_SIZE, DOMINO_BACK


class HalfDomino:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        # self.is_on_board = False
        # self.is_in_stock = True
        # self.orientation = 'top'  # initial half domino orientation
        # if something is done by the player, self.orientation = either left,
        # right, top or bottom

        self.x = 0
        self.y = 0
        self.calcPos()

    def calcPos(self):
        # calculate x and y position based on the current row and column
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    # def placeOnBoard(self):
    #     # change state of the half domino
    #     self.is_on_board = True

    # def drawFromStock(self):
    #     # change state of the half domino
    #     self.is_in_stock = False

    def changeOrientation(self):
        # change state of the half domino
        pass

    def draw(self, win):
        DOMINO_IMAGE = pygame.transform.scale(
            pygame.image.load(f"assets/dom_{self.value}.png"), (40, 40))
        DOMINO_IMAGE_RECT = DOMINO_IMAGE.get_rect(center=(self.x, self.y))
        win.blit(DOMINO_IMAGE, DOMINO_IMAGE_RECT)
        # rotate the image if necessary depending on self.direction

    def drawHidden(self, win):
        DOMINO_BACK_RECT = DOMINO_BACK.get_rect(center=(self.x, self.y))
        win.blit(DOMINO_BACK, DOMINO_BACK_RECT)

    def fromHandToBoard(self, row, col):
        self.row = row
        self.col = col
        self.calcPos()

    def __repr__(self):
        return str(self.value)
