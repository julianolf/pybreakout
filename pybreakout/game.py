import pygame

from . import settings, sprites


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(settings.TITLE)
        self.screen = pygame.display.set_mode(settings.WIN_SIZE)
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.font = pygame.font.Font(settings.FONT, settings.FONT_SIZE)

    def reset(self):
        self.sprites.empty()
        self.bricks.empty()
        self.wall = []
        self.stack_bricks()
        self.paddle = sprites.Paddle((self.sprites,))
        self.ball = sprites.Ball(self, (self.sprites,))
        self.spare_balls = 2
        self.score = 0
        self.running = True

    def stack_bricks(self):
        layers = (self.sprites, self.bricks)
        for i in range(len(settings.BRICK_LINES)):
            color = settings.BRICK_COLORS[i]
            y = settings.BRICK_LINES[i]
            for x in settings.BRICK_COLUMNS:
                brick = sprites.Brick(color, (x, y), layers)
                self.wall.append(brick)

    def breakout(self, color):
        self.score += settings.POINTS.get(color, 0)

    def out(self):
        if self.spare_balls:
            self.spare_balls -= 1
            self.ball = sprites.Ball(self, (self.sprites,))
        else:
            self.running = False

    def update(self):
        self.sprites.update()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.sprites.draw(self.screen)
        self.draw_text(f'{self.spare_balls:>02}', settings.TEXT_LEFT)
        self.draw_text(f'{self.score:>03}', settings.TEXT_CENTER)
        pygame.display.flip()

    def draw_text(self, text, position):
        surface = self.font.render(text, True, settings.WHITE)
        rect = surface.get_rect()
        rect.topleft = position
        self.screen.blit(surface, rect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

    def loop(self):
        while self.running:
            self.clock.tick(settings.FPS)
            self.update()
            self.draw()
            self.events()

    def run(self):
        self.reset()
        self.loop()
        pygame.quit()


def main():
    Game().run()


if __name__ == '__main__':
    main()
