from os import path

TITLE = 'PyBREAKOUT'
WIDTH, HEIGHT = (600, 700)
WIN_SIZE = (WIDTH, HEIGHT)
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BRICK_W, BRICK_H = (40, 12)
BRICK_SIZE = (BRICK_W, BRICK_H)
BRICK_COLORS = (RED, RED, ORANGE, ORANGE, GREEN, GREEN, YELLOW, YELLOW)
BRICK_LINES = tuple(range(100, BRICK_H * len(BRICK_COLORS) + 100, BRICK_H))
BRICK_COLUMNS = tuple(range(0, WIDTH, BRICK_W))
PADDLE_SIZE = (80, 12)
BALL_SIZE = (14, 14)
BALL_RADIUS = 7
ASSETS_PATH = path.join(path.dirname(__file__), 'assets')
SFX = path.join(ASSETS_PATH, 'sfx')
FONT = path.join(ASSETS_PATH, 'font', 'Teko-Regular.ttf')
FONT_SIZE = 70
TEXT_LEFT = (WIDTH * 0.1, 5)
TEXT_CENTER = (WIDTH * 0.5 + 10, 5)
POINTS = {YELLOW: 2, GREEN: 3, ORANGE: 5, RED: 7}
