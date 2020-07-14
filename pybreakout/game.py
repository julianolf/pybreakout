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

    def reset(self):
        self.sprites.empty()
        self.bricks.empty()
        self.wall = []
        self.stack_bricks()
        self.running = True

    def stack_bricks(self):
        layers = (self.sprites, self.bricks)
        for i in range(len(settings.BRICK_LINES)):
            color = settings.BRICK_COLORS[i]
            y = settings.BRICK_LINES[i]
            for x in settings.BRICK_COLUMNS:
                brick = sprites.Brick(color, (x, y), layers)
                self.wall.append(brick)

    def update(self):
        self.sprites.update()

    def draw(self):
        self.screen.fill(settings.BLACK)
        self.sprites.draw(self.screen)
        pygame.display.flip()

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
