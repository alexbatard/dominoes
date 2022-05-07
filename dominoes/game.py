# import pygame
from dominoes.board import Board


class Game:

    def __init__(self, win):
        self.selected_piece = None  # have we selected a piece?
        self.board = Board()
        self.turn = 'player1'  # whose turn is it?
        self.valid_moves = {}  # current valid moves
        self.win = win  # game window

    def updateBoard(self):
        # update the board
        self.board.draw(self.win)
        # pygame.display.update()
