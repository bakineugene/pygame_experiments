from pygame import QUIT, KEYDOWN, K_ESCAPE, draw, init, time, display, Surface, event, K_LEFT, K_RIGHT, K_UP, K_DOWN, KEYDOWN, KEYUP, K_EQUALS, K_MINUS

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

def draw_square_grid_element(surface, colour, size, point):
    x = point[0] * size
    xp = x + size
    y = point[1] * size
    yp = y + size
    draw.lines(surface, colour, True, ((x, y), (x, yp), (xp, yp), (xp, y)))

def draw_grid(surface, colour, size, size_x, size_y):
    for x in range(size_x):
        for y in range(size_y):
            draw_hex_grid_element(surface, colour, size, (x, y))

def draw_hex_grid_element(surface, colour, size, point):
    h = 1.7320508 * size
    w = 2 * size
    x = point[0] * w * 3 / 4 + w
    y = point[1] * h
    if point[0] % 2:
        y = y + h / 2
    p1 = (x, y)
    p2 = (p1[0] + w / 2, p1[1])
    p3 = (p2[0] + w / 4, p2[1] + h / 2)
    p4 = (p3[0] - w / 4, p3[1] + h / 2)
    p5 = (p4[0] - w / 2, p4[1])
    p6 = (p5[0] - w / 4, p5[1] - h / 2) 
    draw.aalines(surface, colour, True, (p1, p2, p3, p4, p5, p6))

class Game(object):

    def __init__(self):
        self.is_running = True
        self.grid_position = (0, 0)
        self.scrolling = (0, 0)
        self.zoom = ZOOM

        self.scroll_left = 0
        self.scroll_up = 0
        self.clock = time.Clock()

        init()

        self.screen = display.set_mode(RESOLUTION_DEFAULT)

        self.background = Surface(self.screen.get_size())
        self.background.fill(COLOR_WHITE)
        self.background = self.background.convert()

        self.make_grid()

    def make_grid(self):
        self.grid = Surface((self.zoom * MAP_SIZE + 1, self.zoom * MAP_SIZE + 1))
        self.grid.fill(COLOR_WHITE)
        draw_grid(self.grid, COLOR_BLACK, self.zoom, 20, 20)
        self.grid = self.grid.convert_alpha()
        self.draw()


    def draw(self):
        self.grid_position = (self.grid_position[0] + self.scrolling[0], self.grid_position[1] + self.scrolling[1])
        self.screen.blit(self.background, POSITION_ZERO)
        self.screen.blit(self.grid, self.grid_position)
        display.flip()

    def start(self):
        while self.is_running:
            self.clock.tick(FPS)
            for e in event.get():
                # handle_events_debug(e, self)
                handle_events_quit(e, self)
                self.handle_grid_scroll(e)
                self.handle_grid_zoom(e)
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

    def handle_grid_zoom(self, event):
        if event.type == KEYDOWN:
            if event.key == K_EQUALS:
                self.zoom = self.zoom + 10
                self.make_grid()
            if event.key == K_MINUS:
                if self.zoom > 10:
                    self.zoom = self.zoom - 10
                    self.make_grid()

game = Game()
game.start()