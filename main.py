import pygame
from dominoes.constants import WIDTH, HEIGHT
from dominoes.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set window dimensions
pygame.display.set_caption('Dominoes')  # set window caption

FPS = 60  # frames per second


def main():
    # main game loop
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:  # event loop
        clock.tick(FPS)  # set FPS

        for event in pygame.event.get():  # check if event happened
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        game.update()

    pygame.quit()


main()

# When 2, 3 or 4 players are playing on the same computer,
# the current player needs to press a button to start his turn.
# His dominoes are then displayed on the screen (under the board).
# When he presses the same button, his turn ends and
# his dominoes are hidden.
# This allows the game to display both players' dominoes,
# but not at the same time, and to set a time limit for 1 turn.

# the game must also display the back of the opponent's dominoes
# so that the other player knows the number of dominoes his oppenent has left
# without seeing the opponent's dominoes'.
