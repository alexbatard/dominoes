import pygame
import sys
from dominoes.constants import WIDTH, HEIGHT, TEAL, LIGHT_CYAN, BLACK, WHITE
from gui.constants import SMALL_FONT, DOMINOES_TEXT, PLAY_TEXT, QUIT_TEXT,\
     DOMINOES_RECT, PLAY_RECT, QUIT_RECT, BUTTON
from dominoes.game import Game
from gui.button import Button

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set window dimensions
pygame.display.set_caption("Main menu")  # set window caption

FPS = 60  # frames per second


def main_menu():  # main menu screen
    pygame.display.set_caption('Main menu')

    while True:
        WIN.fill(TEAL)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(pos=(WIDTH / 3, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="PLAY")

        QUIT_BUTTON = Button(pos=(2 * WIDTH / 3, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="QUIT")

        WIN.blit(DOMINOES_TEXT, DOMINOES_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeTextColor(MENU_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                # if WIDTH / 3 - 60 <= MENU_MOUSE_POS[0] <= WIDTH / 3 + 60 and\
                #         HEIGHT / 2 - 25 <= MENU_MOUSE_POS[1] <= HEIGHT / 2\
                #         + 25:
                    # name_selection()

                # elif 2 * WIDTH / 3 - 60 <= MENU_MOUSE_POS[0] <= 2 * \
                #         WIDTH / 3 + 60 and HEIGHT / 2 - \
                #         50 <= MENU_MOUSE_POS[1] <= HEIGHT / 2 + 50:
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

            # pygame.draw.rect(WIN, LIGHT_CYAN,
            #                  [WIDTH / 3 - 60, HEIGHT / 2 - 25, 120, 50])
            # pygame.draw.rect(WIN, LIGHT_CYAN,
            #                  [2 * WIDTH / 3 - 60, HEIGHT / 2 - 25, 120, 50])

            # WIN.blit(PLAY_TEXT, PLAY_RECT)
            # WIN.blit(QUIT_TEXT, QUIT_RECT)

        pygame.display.update()


def name_selection():
    pygame.display.set_caption("Name selection")
    PLAYER1_NAME_INPUT = ''
    PLAYER2_NAME_INPUT = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                PLAYER1_NAME_INPUT += event.unicode

            WIN.fill(TEAL)
            PLAYER1_NAME = SMALL_FONT.render(PLAYER1_NAME_INPUT, True, BLACK)
            PLAYER2_NAME = SMALL_FONT.render(PLAYER2_NAME_INPUT, True, BLACK)
            WIN.blit(PLAYER1_NAME, (0, 0))

        pygame.display.update()


def play():  # main game loop
    pygame.display.set_caption("Play")
    clock = pygame.time.Clock()
    game = Game(WIN)

    while True:  # event loop
        clock.tick(FPS)  # set FPS
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():  # check if event happened
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        game.updateBoard()


main_menu()

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
