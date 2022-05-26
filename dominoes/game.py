from dominoes.board import Board
from .constants import PLAYER1, PLAYER2, ROWS


class Game:
    cnt = 0
    previous_turn = None
    value_1 = 0
    value_2 = 0

    def __init__(self, win):
        self._init()
        self.win = win  # game window

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = PLAYER1
        self.valid_moves = {}

    def reset(self):
        self._init()

    def update(self):
        # update the board
        self.board.draw(self.win, self.turn)

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.getPiece(row, col)
            if piece != 'x' and piece.player == self.turn:
                self.selected = piece
                # self.valid_moves = self.board.get_valid_moves(piece)
                return True

        return False

    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 'x':
            # and (row, col) in self.valid_moves:
            self.board.fromHandToBoard(self.selected, row, col)
            Game.cnt += 1
            if Game.cnt == 1:
                Game.value_1 = self.selected.value
            elif Game.cnt == 2:
                Game.value_2 = self.selected.value
                Game.cnt = 0
                # self.changeTurn()
                self.removeDominoFromHand(Game.value_1, Game.value_2)
        else:
            return False

        return True

    def changeTurn(self):
        if self.turn == PLAYER1:
            self.turn = PLAYER2
        else:
            self.turn = PLAYER1

    def resetTurn(self):
        Game.previous_turn = self.turn
        self.turn = None

    def restoreTurn(self):
        self.turn = Game.previous_turn

    def removeDominoFromHand(self, value_1, value_2):
        if self.turn == PLAYER1:
            if (value_1, value_2) in self.board.player1_dominoes:
                self.board.player1_dominoes.remove((value_1, value_2))
            else:
                self.board.player1_dominoes.remove((value_2, value_1))
        else:
            if (value_1, value_2) in self.board.player2_dominoes:
                self.board.player2_dominoes.remove((value_1, value_2))
            else:
                self.board.player2_dominoes.remove((value_2, value_1))

    def draw(self):
        if self.turn == PLAYER1:
            row = ROWS - 2
            for piece in self.board.board[row]:
                if piece == 'x':
                    col = self.board.board[row].index(piece)
                    break
            domino_value = self.board.drawPiece(row, col, PLAYER1)
            self.board.player1_dominoes.append(domino_value)
        else:
            row = 0
            for piece in self.board.board[row]:
                if piece == 'x':
                    col = self.board.board[row].index(piece)
                    break
            domino_value = self.board.drawPiece(row, col, PLAYER2)
            self.board.player2_dominoes.append(domino_value)

    def winner(self):
        return self.board.winner()
