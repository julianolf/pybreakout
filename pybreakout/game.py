from os import path

import pygame

from . import settings, sprites


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(settings.TITLE)
        self.screen = pygame.display.set_mode(settings.WIN_SIZE)
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()
        self.bricks = pygame.sprite.Group()
        self.sfx = {
            sound: pygame.mixer.Sound(path.join(settings.SFX, f'{sound}.wav'))
            for sound in ('bounce', 'explosion', 'launch', 'level')
        }

    def reset(self):
        self.sprites.empty()
        self.bricks.empty()
        self.status = sprites.Status(2, 0, (self.sprites,))
        self.wall = []
        self.stack_bricks()
        self.paddle = sprites.Paddle((self.sprites,))
        self.spare_balls = 2
        self.score = 0
        self.speed = 5
        self.splash_screen = None
        self.launch()

    def start(self):
        self.sprites.empty()
        self.splash_screen = sprites.SplashScreen(
            settings.TITLE, (self.sprites,)
        )

    def over(self):
        self.sprites.empty()
        self.splash_screen = sprites.SplashScreen('GAME OVER', (self.sprites,))

    def stack_bricks(self):
        layers = (self.sprites, self.bricks)
        for i in range(len(settings.BRICK_LINES)):
            color = settings.BRICK_COLORS[i]
            y = settings.BRICK_LINES[i]
            for x in settings.BRICK_COLUMNS:
                brick = sprites.Brick(color, (x, y), layers)
                self.wall.append(brick)

    def breakout(self, brick):
        self.score += settings.POINTS.get(brick.color, 0)
        self.status.score = self.score
        self.wall.remove(brick)
        self.sfx['explosion'].play()
        if not self.wall:
            self.level_up()

    def launch(self):
        self.ball = sprites.Ball(self, self.speed, (self.sprites,))
        self.sfx['launch'].play()

    def out(self):
        if self.spare_balls:
            self.spare_balls -= 1
            self.status.spare_balls = self.spare_balls
            self.launch()
        else:
            self.over()

    def level_up(self):
        self.sfx['level'].play()
        self.sprites.remove((self.ball,))
        self.ball.kill()
        self.stack_bricks()
        self.speed += 2
        self.launch()

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
            if event.type == pygame.KEYDOWN:
                if self.splash_screen:
                    self.reset()
                    return

    def loop(self):
        while self.running:
            self.clock.tick(settings.FPS)
            self.update()
            self.draw()
            self.events()

    def run(self):
        self.running = True
        self.start()
        self.loop()
        pygame.quit()


def main():
    Game().run()


if __name__ == '__main__':
    main()
