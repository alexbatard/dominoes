import unittest
import pygame
from dominoes.board import Board
from dominoes.half_domino import HalfDomino
from dominoes.game import Game
from dominoes.constants import WIDTH, HEIGHT, SQUARE_SIZE


class Tests(unittest.TestCase):
    def test_init(self):
        board = Board(2, 7)
        half_domino = HalfDomino(0, 1, 5)
        game = Game(pygame.display.set_mode((WIDTH, HEIGHT)))
        self.assertEqual(board.nb_players, 2)
        self.assertEqual(board.nb_dominoes_per_player, 7)
        self.assertEqual(half_domino.row, 0)
        self.assertEqual(half_domino.col, 1)
        self.assertEqual(half_domino.value, 5)
        self.assertEqual(game.win, pygame.display.set_mode((WIDTH, HEIGHT)))

    def test_type(self):
        board = Board(2, 7)
        half_domino = HalfDomino(0, 1, 5)
        game = Game(pygame.display.set_mode((WIDTH, HEIGHT)))
        self.assertEqual(type(board), Board)
        self.assertEqual(type(half_domino), HalfDomino)
        self.assertEqual(type(game), Game)

    def test_fill_domino_values(self):
        board = Board(2, 7)
        board.fill_domino_values()
        self.assertEqual(len(board.domino_values), 28)

    def test_create_board(self):
        board = Board(2, 2)
        self.assertEqual(len(board.board), 16)
        self.assertEqual(len(board.board[0]), 10)

    def test_calc_pos(self):
        half_domino = HalfDomino(0, 1, 5)
        self.assertEqual(half_domino.x, SQUARE_SIZE + SQUARE_SIZE // 2)
        self.assertEqual(half_domino.y, SQUARE_SIZE // 2)


if __name__ == "__main__":
    unittest.main()
