import pygame
from dominoes.board import Board

players = 2
dominoes_per_player = 7


class Game:
    def __init__(self, win):
        self.selected_piece = None  # have we selected a piece?
        self.board = Board(players, dominoes_per_player)
        self.turn = 'player1'  # whose turn is it?
        self.valid_moves = {}  # current valid moves
        self.win = win

    def update(self):
        self.board.draw_background()
        pygame.display.update()
