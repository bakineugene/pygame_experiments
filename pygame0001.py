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


class Game(object):

    def __init__(self):
        self.is_running = True

        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION_DEFAULT)

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(COLOR_WHITE)
        self.background.convert()

        self.screen.blit(self.background, POSITION_ZERO)

    def draw(self):
        pygame.display.flip()

    def start(self):
        while game.is_running:
            for event in pygame.event.get():
                handle_events_debug(event, game)
                handle_events_quit(event, game)
            game.draw()

game = Game()
game.start()