import pygame

RESOLUTION_DEFAULT = (640, 480)

POSITION_ZERO = (0, 0)

COLOR_WHITE = (255, 255, 255)

def handle_events_debug(event, game):
    print(event)

def handle_events_quit(event, game):
    if event.type == pygame.QUIT:
        game.is_running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game.is_running = False


class GameState(object):

    def __init__(self):
        self.is_running = True


def game_init():
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION_DEFAULT)

    background = pygame.Surface(screen.get_size())
    background.fill(COLOR_WHITE)
    background.convert()

    screen.blit(background, POSITION_ZERO)

    game = GameState()

    while game.is_running:
        for event in pygame.event.get():
            handle_events_debug(event, game)
            handle_events_quit(event, game)

        pygame.display.flip()


game_init()