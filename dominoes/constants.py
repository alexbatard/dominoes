import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600 + 6 * 40
ROWS, COLS = 21, 15
SQUARE_SIZE = WIDTH // COLS

# rgb
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CRIMSON_RED = (220, 20, 60)
LIGHT_CYAN = (224, 255, 255)
PALE_TURQUOISE = (175, 238, 238)
TEAL = (0, 128, 128)
AMBER = (255, 179, 0)
PURPLE = (170, 0, 255)

# domino back image
DOMINO_BACK = pygame.transform.scale(
    pygame.image.load("assets/dom_back.png"), (40, 40))

# players
PLAYER1 = 'player1'
PLAYER2 = 'player2'
