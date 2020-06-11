from pygame import QUIT, KEYDOWN, K_ESCAPE, draw, init, time, display, Surface, event, K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYDOWN, KEYUP

RESOLUTION_DEFAULT = (1024, 768)

POSITION_ZERO = (0, 0)
SCROLL_SPEED = 5
FPS = 60
MAP_SIZE = 100
ZOOM = 60

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)

def handle_events_debug(event, game):
    print(event)

def handle_events_quit(event, game):
    if event.type == QUIT:
        game.is_running = False
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            game.is_running = False

def draw_grid_element(surface, colour, size, point):
    point_plus_x = point[0] + size
    point_plus_y = point[1] + size
    draw.lines(surface, colour, True, (point, (point[0], point_plus_y), (point_plus_x, point_plus_y), (point_plus_x, point[1])))

def draw_grid(surface, colour=COLOR_BLACK, size=ZOOM, size_x=MAP_SIZE, size_y=MAP_SIZE):
    for x in range(size_x):
        for y in range(size_y):
            draw_grid_element(surface, colour, size, (x * size, y * size))

class Game(object):

    def __init__(self):
        self.is_running = True
        self.grid_position = (0, 0)
        self.scrolling = (0, 0)

        self.scroll_left = 0
        self.scroll_up = 0
        self.clock = time.Clock()

        init()

        self.screen = display.set_mode(RESOLUTION_DEFAULT)

        self.background = Surface(self.screen.get_size())
        self.background.fill(COLOR_WHITE)
        self.background = self.background.convert()

        self.grid = Surface((ZOOM*MAP_SIZE, ZOOM*MAP_SIZE))
        self.grid.fill(COLOR_WHITE)
        draw_grid(self.grid)
        
        self.grid = self.grid.convert_alpha()

    def draw(self):
        self.grid_position = (self.grid_position[0] + self.scrolling[0], self.grid_position[1] + self.scrolling[1])
        self.screen.blit(self.background, POSITION_ZERO)
        self.screen.blit(self.grid, self.grid_position)
        display.flip()

    def start(self):
        while self.is_running:
            self.clock.tick(FPS)
            for e in event.get():
                handle_events_debug(e, self)
                handle_events_quit(e, self)
                self.handle_grid_scroll(e)
            self.draw()

    def handle_grid_scroll(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.scrolling = (-SCROLL_SPEED, self.scrolling[1])
            if event.key == K_LEFT:
                self.scrolling = (SCROLL_SPEED, self.scrolling[1])
            if event.key == K_UP:
                self.scrolling = (self.scrolling[0], SCROLL_SPEED)
            if event.key == K_DOWN:
                self.scrolling = (self.scrolling[0], -SCROLL_SPEED)
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                self.scrolling = (0, self.scrolling[1])
            if event.key == K_LEFT:
                self.scrolling = (0, self.scrolling[1])
            if event.key == K_UP:
                self.scrolling = (self.scrolling[0], 0)
            if event.key == K_DOWN:
                self.scrolling = (self.scrolling[0], 0)


game = Game()
game.start()