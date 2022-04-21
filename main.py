import pygame
from dominoes.constants import WIDTH, HEIGHT
from dominoes.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set window dimensions
pygame.display.set_caption('Dominoes')  # set window caption

FPS = 60

players = 2
dominoes_per_player = 7


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(players, dominoes_per_player)  # create a board

    while run:  # event loop
        clock.tick(FPS)  # set FPS

        for event in pygame.event.get():  # check if event happened
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(WIN)
        pygame.display.update()

    pygame.quit()


main()

# When 2 or 4 players are playing on the same computer,
# the current player needs to press a button to start his turn.
# His dominoes are then displayed on the screen (under the board).
# When he presses the same button, his turn ends and
# his dominoes are hidden.
# This allows the game to display both players' dominoes,
# but not at the same time, and to set a time limit for 1 turn

# the game must also display the back of the opponent's dominoes on top
# so that the other player knows the number of dominoes his oppenent has left
