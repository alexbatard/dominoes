from .constants import SQUARE_SIZE


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

    def draw(self, win):
        # draw half domino on the window
        pass
        # format a str with self.value to select the right image
        # ex for selecting the right image:
        # f"half_domino_{domino.value}.jpg"
        # rotate the image if necessary depending on self.direction

    def __repr__(self):
        return str(self.value)
