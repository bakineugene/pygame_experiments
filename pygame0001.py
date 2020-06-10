import pygame

RESOLUTION_DEFAULT = (640, 480)

POSITION_ZERO = (0, 0)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

def handle_events_debug(event, game):
    print(event)

def handle_events_quit(event, game):
    if event.type == pygame.QUIT:
        game.is_running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            game.is_running = False

def draw_grid_element(surface, colour, size, point):
    point_plus = point + size
    pygame.draw.lines(surface, colour, True, ((point, point), (point, point_plus), (point_plus, point_plus), (point_plus, point)))

def draw_grid(surface, colour=COLOR_BLACK, size=20):
    draw_grid_element(surface, colour, size, 0)
    draw_grid_element(surface, colour, size, size)
    draw_grid_element(surface, colour, size, size * 2)
    draw_grid_element(surface, colour, size, size * 3)
    draw_grid_element(surface, colour, size, size * 4)

class Game(object):

    def __init__(self):
        self.is_running = True
        self.timer = 1

        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION_DEFAULT)

        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(COLOR_WHITE)
        self.background = self.background.convert()

        self.grid = pygame.Surface(self.screen.get_size())
        self.grid.fill(COLOR_WHITE)
        draw_grid(self.grid)
        
        self.grid = self.grid.convert_alpha()

    def draw(self):
        self.timer = self.timer + 1
        self.screen.blit(self.background, POSITION_ZERO)
        self.screen.blit(self.grid, (POSITION_ZERO[0] + self.timer, POSITION_ZERO[1]))
        pygame.display.flip()

    def start(self):
        while game.is_running:
            for event in pygame.event.get():
                handle_events_debug(event, game)
                handle_events_quit(event, game)
            game.draw()

game = Game()
game.start()