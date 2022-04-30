import pygame
from dominoes.constants import BLACK, WIDTH, HEIGHT

pygame.init()

# fonts
SMALL_FONT = pygame.font.SysFont('cambria', 20)
BIG_FONT = pygame.font.SysFont('cambria', 80)

# text (type Surface)
DOMINOES_TEXT = BIG_FONT.render('Dominoes', True, BLACK)
PLAY_TEXT = SMALL_FONT.render('Play', True, BLACK)
QUIT_TEXT = SMALL_FONT.render('Quit', True, BLACK)

# rectangles
# a new rectangle covering the entire surface
# this rectangle will always start at (0, 0)
# with a width and height the same size as the image
# the rectangles are centered at the given positions
DOMINOES_RECT = DOMINOES_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 3))
PLAY_RECT = PLAY_TEXT.get_rect(center=(WIDTH / 3, HEIGHT / 2))
QUIT_RECT = QUIT_TEXT.get_rect(center=(2 * WIDTH / 3, HEIGHT / 2))

# button image
BUTTON = pygame.transform.scale(pygame.image.load("assets/button.png"),
                                (200, 100))
