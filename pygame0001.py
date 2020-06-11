import pygame

RESOLUTION_DEFAULT = (1024, 768)

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
    point_plus_x = point[0] + size
    point_plus_y = point[1] + size
    pygame.draw.lines(surface, colour, True, (point, (point[0], point_plus_y), (point_plus_x, point_plus_y), (point_plus_x, point[1])))

def draw_grid(surface, colour=COLOR_BLACK, size=60, size_x=100, size_y=100):
    for x in range(size_x):
        for y in range(size_y):
            draw_grid_element(surface, colour, size, (x * size, y * size))

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
        self.screen.blit(self.grid, POSITION_ZERO)
        pygame.display.flip()

    def start(self):
        while game.is_running:
            for event in pygame.event.get():
                handle_events_debug(event, game)
                handle_events_quit(event, game)
            game.draw()

game = Game()
game.start()