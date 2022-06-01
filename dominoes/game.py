import numpy as np
from dominoes.board import Board
from .constants import PLAYER1, PLAYER2, ROWS, COLS


class Game:
    '''
    This class manages the operation of the game.
    It allows the interaction between the two other
    classes: Board and HalfDomino.
    '''
    piece_nb = 1
    value_1 = 0
    value_2 = 0
    piece_1 = 0
    piece_2 = 0

    def __init__(self, win):
        self._init()
        self.win = win  # game window

    def _init(self):
        '''
        Initializes the game object.
        '''
        self.selected = None
        self.board = Board()
        self.turn = PLAYER1
        self.previous_turn = None
        self.turn_nb = 1
        self.valid_moves = []
        self.end_dominoes = []
        self.dominoes_in_stock = len(self.board.domino_values)

    def reset(self):
        '''
        Resets the game.
        '''
        self._init()

    def update(self):
        '''
        Updates the game window.
        '''
        # update the board
        self.board.draw(self.win, self.turn)

    def select(self, row, col):
        '''
        Selects a half-domino.
        '''
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.getPiece(row, col)
            if piece != 'x' and piece.player == self.turn:
                self.selected = piece
                self.valid_moves = self.getValidMoves(self.selected)
                return True

        return False

    def _move(self, row, col):
        '''
        Allows the movement of a half-domino on the board
        if it is selected and the square where it is to be placed
        is free and is one of the allowed squares.
        Also removes this half-domino from the player's hand.
        '''
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 'x' and (row, col) in self.valid_moves:
            self.board.fromHandToBoard(self.selected, row, col)
            self.board.getNeighbors(self.selected)
            if Game.piece_nb == 1:
                Game.piece_1 = self.selected
                Game.piece_nb += 1
            elif Game.piece_nb == 2:
                Game.piece_2 = self.selected
                Game.piece_nb -= 1
                self.board.getNeighbors(Game.piece_1)
                self.updateEndDominoes(Game.piece_1, Game.piece_2)
                self.removeDominoFromHand(Game.piece_1.value,
                                          Game.piece_2.value)
                self.turn_nb += 1
                self.resetTurn()
        else:
            return False

        return True

    def checkNeighbors(self, row, col):
        '''
        Checks for neighbors at the given row and column and
        sets the valid moves.
        '''
        top, bottom, left, right = 1, 1, 1, 1
        if self.board.getPiece(row - 1, col) != 'x':
            top = 0
        if self.board.getPiece(row + 1, col) != 'x':
            bottom = 0
        if self.board.getPiece(row, col - 1) != 'x':
            left = 0
        if self.board.getPiece(row, col + 1) != 'x':
            right = 0
        directions = np.array([(top, top), (bottom, bottom), (left, left),
                               (right, right)])

        if bottom + right + top + left == 3:
            available_directions = directions * np.array([(row - 1, col),
                                                          (row + 1, col),
                                                          (row, col - 1),
                                                          (row, col + 1)])
            for direction in available_directions.tolist():
                self.valid_moves.append(tuple(direction))

    def updateEndDominoes(self, piece_1, piece_2):
        '''
        Updates the instance variable end_dominoes.
        '''
        for domino in self.end_dominoes:
            for i in range(len(domino)):
                self.board.getNeighbors(domino[i])
        if self.turn_nb > 2:
            for domino in self.end_dominoes:
                if domino[0].getNeighborNumber(
                ) > 1 and domino[1].getNeighborNumber() > 1:
                    self.end_dominoes.remove(domino)
        self.end_dominoes.append((piece_1, piece_2))

    def browseMovesAngle(self, piece_1, piece_2):
        '''
        Returns a list of the allowed moves for the placement
        of the first half-domino according to the position
        of the previous domino, in case the last two dominoes form an angle.
        '''
        moves = []
        if piece_1.neighbors['left'] == 1 and piece_2.neighbors['top'] == 1:
            moves.append((piece_2.row + 1, piece_2.col))
            moves.append((piece_2.row, piece_2.col + 1))
        elif piece_1.neighbors['left'] == 1 and piece_2.neighbors[
                'bottom'] == 1:
            moves.append((piece_2.row - 1, piece_2.col))
            moves.append((piece_2.row, piece_2.col + 1))
        elif piece_1.neighbors['right'] == 1 and piece_2.neighbors['top'] == 1:
            moves.append((piece_2.row + 1, piece_2.col))
            moves.append((piece_2.row, piece_2.col - 1))
        elif piece_1.neighbors['right'] == 1 and piece_2.neighbors[
                'bottom'] == 1:
            moves.append((piece_2.row - 1, piece_2.col))
            moves.append((piece_2.row, piece_2.col - 1))
        elif piece_1.neighbors['top'] == 1 and piece_2.neighbors['left'] == 1:
            moves.append((piece_2.row, piece_2.col + 1))
            moves.append((piece_2.row + 1, piece_2.col))
        elif piece_1.neighbors['top'] == 1 and piece_2.neighbors['right'] == 1:
            moves.append((piece_2.row, piece_2.col - 1))
            moves.append((piece_2.row + 1, piece_2.col))
        elif piece_1.neighbors['bottom'] == 1 and piece_2.neighbors[
                'left'] == 1:
            moves.append((piece_2.row, piece_2.col + 1))
            moves.append((piece_2.row - 1, piece_2.col))
        elif piece_1.neighbors['bottom'] == 1 and piece_2.neighbors[
                'right'] == 1:
            moves.append((piece_2.row, piece_2.col - 1))
            moves.append((piece_2.row - 1, piece_2.col))
        return moves

    def browseMovesStraight(self, piece):
        '''
        Returns a list of the allowed moves for the
        placement of the first half-domino according
        to the position of the previous domino, in the case the
        last two dominoes are aligned.
        '''
        moves = []
        if piece.neighbors['top'] == 0:
            moves.append((piece.row - 1, piece.col))
        if piece.neighbors['bottom'] == 0:
            moves.append((piece.row + 1, piece.col))
        if piece.neighbors['left'] == 0:
            moves.append((piece.row, piece.col - 1))
        if piece.neighbors['right'] == 0:
            moves.append((piece.row, piece.col + 1))
        return moves

    def getValidMoves(self, piece):
        '''
        Browses all the possible game situations to return
        the corresponding allowed moves,
        using the methods browseMovesAngle() and browseMovesStraight().
        '''
        moves = []
        if self.turn_nb == 1:
            for row in range(3, ROWS - 3):
                for col in range(COLS):
                    moves.append((row, col))
            return moves
        elif Game.piece_nb == 1:
            for domino in self.end_dominoes:
                if (domino[0].neighbors['top'] == 1
                        or domino[0].neighbors['bottom']
                        == 1) and (domino[0].neighbors['left'] == 1
                                   or domino[0].neighbors['right'] == 1):
                    if domino[0].value == piece.value:
                        moves += self.browseMovesAngle(domino[0], domino[1])
                elif (domino[1].neighbors['top'] == 1
                      or domino[1].neighbors['bottom']
                      == 1) and (domino[1].neighbors['left'] == 1
                                 or domino[1].neighbors['right'] == 1):
                    if domino[1].value == piece.value:
                        moves += self.browseMovesAngle(domino[1], domino[0])
                else:
                    if self.turn_nb == 2:
                        if domino[0].value == piece.value:
                            moves += self.browseMovesStraight(domino[0])
                        if domino[1].value == piece.value:
                            moves += self.browseMovesStraight(domino[1])
                    elif domino[0].getNeighborNumber(
                    ) == 1 and domino[0].value == piece.value:
                        moves += self.browseMovesStraight(domino[0])
                    elif domino[1].value == piece.value:
                        moves += self.browseMovesStraight(domino[1])
            return moves
        else:
            if Game.piece_1.neighbors['top'] == 1:
                prev_piece = self.board.getPiece(Game.piece_1.row - 1,
                                                 Game.piece_1.col)
            elif Game.piece_1.neighbors['bottom'] == 1:
                prev_piece = self.board.getPiece(Game.piece_1.row + 1,
                                                 Game.piece_1.col)
            elif Game.piece_1.neighbors['left'] == 1:
                prev_piece = self.board.getPiece(Game.piece_1.row,
                                                 Game.piece_1.col - 1)
            elif Game.piece_1.neighbors['right'] == 1:
                prev_piece = self.board.getPiece(Game.piece_1.row,
                                                 Game.piece_1.col + 1)
            self.board.getNeighbors(prev_piece)
            if prev_piece.neighbors['top'] == prev_piece.neighbors[
                    'bottom'] == 1 or prev_piece.neighbors[
                        'left'] == prev_piece.neighbors['right'] == 1:
                return self.browseMovesStraight(Game.piece_1)
            else:
                if Game.piece_1.neighbors['top'] == 1:
                    return [(Game.piece_1.row + 1, Game.piece_1.col)]
                elif Game.piece_1.neighbors['bottom'] == 1:
                    return [(Game.piece_1.row - 1, Game.piece_1.col)]
                elif Game.piece_1.neighbors['left'] == 1:
                    return [(Game.piece_1.row, Game.piece_1.col + 1)]
                elif Game.piece_1.neighbors['right'] == 1:
                    return [(Game.piece_1.row, Game.piece_1.col - 1)]

    def changeTurn(self):
        '''
        Changes the current turn to the other player.
        '''
        if self.turn == PLAYER1:
            self.turn = PLAYER2
        else:
            self.turn = PLAYER1

    def resetTurn(self):
        '''
        Resets the current player.
        '''
        self.previous_turn = self.turn
        self.turn = None

    def restoreTurn(self):
        '''
        Restores the state of the previous turn.
        '''
        self.turn = self.previous_turn

    def removeDominoFromHand(self, value_1, value_2):
        '''
        Removes a domino from the player's hand.
        '''
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

    def pick(self):
        '''
        Adds a randomly chosen domino from the stock to a player
        when the latter draws.
        '''
        self.dominoes_in_stock -= 1
        if self.turn == PLAYER1:
            row = ROWS - 2
            for piece in self.board[row]:
                if piece == 'x':
                    col = self.board[row].index(piece)
                    break
            domino_value = self.board.pickPiece(row, col, PLAYER1)
            self.board.player1_dominoes.append(domino_value)
        else:
            row = 0
            for piece in self.board[row]:
                if piece == 'x':
                    col = self.board[row].index(piece)
                    break
            domino_value = self.board.pickPiece(row, col, PLAYER2)
            self.board.player2_dominoes.append(domino_value)

    def winner(self):
        '''
        Determines the winner of the game.
        '''
        if len(self.board.player1_dominoes) == 0:
            return PLAYER1
        elif len(self.board.player2_dominoes) == 0:
            return PLAYER2

        return None
