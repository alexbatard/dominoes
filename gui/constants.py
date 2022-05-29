import pygame
from dominoes.constants import WIDTH, HEIGHT, AMBER, BLACK

pygame.init()

# fonts
SMALLER_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 28)
SMALL_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 30)
MEDIUM_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 65)
BIG_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 90)

# text (type Surface)
DOMINOES_TEXT = BIG_FONT.render("Dominoes!", True, AMBER)
SELECT_MODE_TEXT = BIG_FONT.render("Select Mode", True, AMBER)
SELECT_COMPUTER_DIFFICULTY_TEXT = MEDIUM_FONT.render(
    "Select computer difficulty", True, AMBER)
ENTER_PLAYER_NAMES_TEXT = BIG_FONT.render("Enter player names", True, AMBER)
PRESS_ENTER_TEXT = MEDIUM_FONT.render("Press Enter to play!", True, AMBER)
PLAYER1_TEXT = MEDIUM_FONT.render("Player 1", True, AMBER)
PLAYER2_TEXT = MEDIUM_FONT.render("Player 2", True, AMBER)
END_GAME_TEXT = BIG_FONT.render("End of the game", True, AMBER)
STOCK_EMPTY_TEXT = SMALL_FONT.render("Stock empty!", True, BLACK)

# rectangles
# a new rectangle covering the entire surface
# this rectangle will always start at (0, 0)
# with a width and height the same size as the image
# the rectangles are centered at the given positions
DOMINOES_RECT = DOMINOES_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 4))
SELECT_MODE_RECT = SELECT_MODE_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 12))
SELECT_COMPUTER_DIFFICULTY_RECT = SELECT_COMPUTER_DIFFICULTY_TEXT.get_rect(
    center=(WIDTH / 2, HEIGHT / 12))
ENTER_PLAYER_NAMES_RECT = ENTER_PLAYER_NAMES_TEXT.get_rect(center=(WIDTH / 2,
                                                                   HEIGHT /
                                                                   12))
PRESS_ENTER_RECT = PRESS_ENTER_TEXT.get_rect(center=(WIDTH / 2,
                                                     2 * HEIGHT / 3))
PLAYER1_RECT = PLAYER1_TEXT.get_rect(center=(WIDTH / 4, HEIGHT / 3))
PLAYER2_RECT = PLAYER2_TEXT.get_rect(center=(3 * WIDTH / 4, HEIGHT / 3))
NAME_TEXT_BOX_1 = pygame.Rect(WIDTH / 4 - 150 / 2, 3 * HEIGHT / 7 - 50 / 2,
                              150, 50)
NAME_TEXT_BOX_2 = pygame.Rect(3 * WIDTH / 4 - 150 / 2, 3 * HEIGHT / 7 - 50 / 2,
                              150, 50)
END_GAME_RECT = END_GAME_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 12))
STOCK_EMPTY_RECT = STOCK_EMPTY_TEXT.get_rect(center=(13 * WIDTH / 15,
                                                     18.5 * HEIGHT / 21))

# images
BUTTON = pygame.transform.scale(pygame.image.load("assets/purple_button.png"),
                                (180, 120))
BACKGROUND = pygame.transform.scale(
    pygame.image.load("assets/retro_background.jpg"), (600, 840))
