import pygame
import sys
from dominoes.constants import WIDTH, HEIGHT, TEAL, LIGHT_CYAN, BLACK, WHITE
from gui.constants import SMALL_FONT, DOMINOES_TEXT, DOMINOES_RECT,\
     SELECT_MODE_TEXT, SELECT_MODE_RECT, BUTTON,\
     SELECT_COMPUTER_DIFFICULTY_TEXT, SELECT_COMPUTER_DIFFICULTY_RECT,\
     BACKGROUND
from dominoes.game import Game
from gui.button import Button

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # set window dimensions
pygame.display.set_caption("Main menu")  # set window caption

FPS = 60  # frames per second


def main_menu():  # main menu screen
    pygame.display.set_caption('Main menu')

    while True:
        # WIN.fill(TEAL)
        WIN.blit(BACKGROUND, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(pos=(WIDTH / 3, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Play")

        QUIT_BUTTON = Button(pos=(2 * WIDTH / 3, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Quit")

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
                    gamemode_menu()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def gamemode_menu():
    pygame.display.set_caption("Gamemode selection")

    while True:
        # WIN.fill(TEAL)
        WIN.blit(BACKGROUND, (0, 0))

        GAMEMODE_MOUSE_POS = pygame.mouse.get_pos()

        TWO_PLAYERS_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 3),
                                    font=SMALL_FONT,
                                    image=BUTTON,
                                    base_color=BLACK,
                                    hovering_color=WHITE,
                                    text_input="2 Players")

        THREE_PLAYERS_BUTTON = Button(pos=(WIDTH / 2, 5 * HEIGHT / 12),
                                      font=SMALL_FONT,
                                      image=BUTTON,
                                      base_color=BLACK,
                                      hovering_color=WHITE,
                                      text_input="3 Players")

        FOUR_PLAYERS_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 2),
                                     font=SMALL_FONT,
                                     image=BUTTON,
                                     base_color=BLACK,
                                     hovering_color=WHITE,
                                     text_input="4 Players")

        COMPUTER_BUTTON = Button(pos=(WIDTH / 2, 7 * HEIGHT / 12),
                                 font=SMALL_FONT,
                                 image=BUTTON,
                                 base_color=BLACK,
                                 hovering_color=WHITE,
                                 text_input="Computer")

        BACK_BUTTON = Button(pos=(WIDTH / 2, 11 * HEIGHT / 12),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Back")

        WIN.blit(SELECT_MODE_TEXT, SELECT_MODE_RECT)

        for button in [
                TWO_PLAYERS_BUTTON, THREE_PLAYERS_BUTTON, FOUR_PLAYERS_BUTTON,
                COMPUTER_BUTTON, BACK_BUTTON
        ]:
            button.changeTextColor(GAMEMODE_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if TWO_PLAYERS_BUTTON.checkForInput(GAMEMODE_MOUSE_POS):
                    name_menu()

                if COMPUTER_BUTTON.checkForInput(GAMEMODE_MOUSE_POS):
                    computer_difficulty_menu()

                if BACK_BUTTON.checkForInput(GAMEMODE_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def computer_difficulty_menu():
    pygame.display.set_caption("Computer difficulty selection")

    while True:
        # WIN.fill(TEAL)
        WIN.blit(BACKGROUND, (0, 0))

        COMPUTER_DIFFICULTY_MOUSE_POS = pygame.mouse.get_pos()

        EASY_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 3),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Easy")

        INTERMEDIATE_BUTTON = Button(pos=(WIDTH / 2, 5 * HEIGHT / 12),
                                     font=SMALL_FONT,
                                     image=BUTTON,
                                     base_color=BLACK,
                                     hovering_color=WHITE,
                                     text_input="Intermediate")

        HARD_BUTTON = Button(pos=(WIDTH / 2, HEIGHT / 2),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Hard")

        BACK_BUTTON = Button(pos=(WIDTH / 2, 11 * HEIGHT / 12),
                             font=SMALL_FONT,
                             image=BUTTON,
                             base_color=BLACK,
                             hovering_color=WHITE,
                             text_input="Back")

        WIN.blit(SELECT_COMPUTER_DIFFICULTY_TEXT,
                 SELECT_COMPUTER_DIFFICULTY_RECT)

        for button in [
                EASY_BUTTON, INTERMEDIATE_BUTTON, HARD_BUTTON, BACK_BUTTON
        ]:
            button.changeTextColor(COMPUTER_DIFFICULTY_MOUSE_POS)
            button.update(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(COMPUTER_DIFFICULTY_MOUSE_POS):
                    gamemode_menu()

        pygame.display.update()


def name_menu():
    pygame.display.set_caption("Name selection")
    PLAYER1_NAME_INPUT = ''
    PLAYER2_NAME_INPUT = ''

    while True:
        # WIN.fill(TEAL)
        WIN.blit(BACKGROUND, (0, 0))
        PLAYER1_NAME = SMALL_FONT.render(PLAYER1_NAME_INPUT, True, BLACK)
        PLAYER2_NAME = SMALL_FONT.render(PLAYER2_NAME_INPUT, True, BLACK)
        WIN.blit(PLAYER1_NAME, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                PLAYER1_NAME_INPUT += event.unicode

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


if __name__ == "__main__":
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
