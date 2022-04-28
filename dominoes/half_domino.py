import pygame
from .constants import SQUARE_SIZE, DOMINO_BACK


class HalfDomino:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.is_on_board = False
        self.is_in_stock = True
        self.orientation = 'top'  # initial half domino orientation
        # if something is done by the player, self.orientation = either left,
        # right, top or bottom

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        # calculate x and y position based on the current row and column
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def place_on_board(self):
        # change state of the half domino
        self.is_on_board = True

    def draw_from_stock(self):
        # change state of the half domino
        self.is_in_stock = False

    def change_orientation(self):
        # change state of the half domino
        pass

    def draw_current_player(self, win):
        domino_image = pygame.transform.scale(
            pygame.image.load(f"assets/dom_{self.value}.png"), (40, 40))
        win.blit(domino_image, (self.x - domino_image.get_width() // 2,
                                self.y - domino_image.get_height() // 2))
        # rotate the image if necessary depending on self.direction

    def draw_opponent(self, win):
        win.blit(DOMINO_BACK, (self.x - DOMINO_BACK.get_width() // 2,
                               self.y - DOMINO_BACK.get_height() // 2))

    def __repr__(self):
        return str(self.value)
