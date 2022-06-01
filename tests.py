import unittest
import pygame
from dominoes.board import Board
from dominoes.half_domino import HalfDomino
from dominoes.game import Game
from gui.button import Button
from dominoes.constants import WIDTH, HEIGHT, SQUARE_SIZE, PLAYER1,\
    BLACK, WHITE
from gui.constants import SMALL_FONT, BUTTON


class Tests(unittest.TestCase):

    def testInit(self):
        board = Board()
        half_domino = HalfDomino(0, 1, 5, PLAYER1)
        game = Game(pygame.display.set_mode((WIDTH, HEIGHT)))
        button = Button(pos=(WIDTH / 2, HEIGHT / 2),
                        font=SMALL_FONT,
                        image=BUTTON,
                        base_color=BLACK,
                        hovering_color=WHITE,
                        text_input="Button")
        self.assertEqual(board.dominoes_per_player, 7)
        self.assertEqual(half_domino.row, 0)
        self.assertEqual(half_domino.col, 1)
        self.assertEqual(half_domino.value, 5)
        self.assertEqual(half_domino.player, PLAYER1)
        self.assertEqual(game.win, pygame.display.set_mode((WIDTH, HEIGHT)))
        self.assertEqual(button.x, WIDTH / 2)
        self.assertEqual(button.y, HEIGHT / 2)

    def testType(self):
        board = Board()
        half_domino = HalfDomino(0, 1, 5, PLAYER1)
        game = Game(pygame.display.set_mode((WIDTH, HEIGHT)))
        button = Button(pos=(WIDTH / 2, HEIGHT / 2),
                        font=SMALL_FONT,
                        image=BUTTON,
                        base_color=BLACK,
                        hovering_color=WHITE,
                        text_input="Button")
        self.assertEqual(type(board), Board)
        self.assertEqual(type(half_domino), HalfDomino)
        self.assertEqual(type(game), Game)
        self.assertEqual(type(button), Button)

    def testFillDominoValues(self):
        board = Board()
        board.fillDominoValues()
        self.assertEqual(len(board.domino_values), 28)

    def testCreateBoard(self):
        board = Board()
        self.assertEqual(len(board), 21)
        self.assertEqual(len(board[0]), 15)

    def testCalcPos(self):
        half_domino = HalfDomino(0, 1, 5, PLAYER1)
        self.assertEqual(half_domino.x, SQUARE_SIZE + SQUARE_SIZE // 2)
        self.assertEqual(half_domino.y, SQUARE_SIZE // 2)


if __name__ == "__main__":
    unittest.main()
