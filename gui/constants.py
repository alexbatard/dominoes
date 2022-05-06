import pygame
from dominoes.constants import BLACK, WIDTH, HEIGHT

pygame.init()

# fonts
SMALL_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 30)
MEDIUM_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 65)
BIG_FONT = pygame.font.Font("assets/SF Atarian System.ttf", 90)

# text (type Surface)
DOMINOES_TEXT = BIG_FONT.render('Dominoes', True, BLACK)
SELECT_MODE_TEXT = BIG_FONT.render('Select Mode', True, BLACK)
SELECT_COMPUTER_DIFFICULTY_TEXT = MEDIUM_FONT.render(
    'Select computer difficulty', True, BLACK)

# rectangles
# a new rectangle covering the entire surface
# this rectangle will always start at (0, 0)
# with a width and height the same size as the image
# the rectangles are centered at the given positions
DOMINOES_RECT = DOMINOES_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 4))
SELECT_MODE_RECT = SELECT_MODE_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 12))
SELECT_COMPUTER_DIFFICULTY_RECT = SELECT_COMPUTER_DIFFICULTY_TEXT.get_rect(
    center=(WIDTH / 2, HEIGHT / 12))

# images
BUTTON = pygame.transform.scale(pygame.image.load("assets/purple_button.png"),
                                (180, 120))
BACKGROUND = pygame.transform.scale(
    pygame.image.load("assets/retro_background.jpg"), (600, 840))
