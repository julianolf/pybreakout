from random import randint

import pygame

from . import settings


class Brick(pygame.sprite.Sprite):
    def __init__(self, color, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image = pygame.Surface(settings.BRICK_SIZE)
        image.fill(settings.BLACK)
        image.set_colorkey(settings.BLACK)
        inner_size = (settings.BRICK_W - 2, settings.BRICK_H - 2)
        pygame.draw.rect(image, color, pygame.Rect((1, 1), inner_size))
        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.color = color


class Paddle(pygame.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image = pygame.Surface(settings.PADDLE_SIZE)
        image.fill(settings.BLACK)
        image.set_colorkey(settings.BLACK)
        pygame.draw.rect(
            image, settings.BLUE, pygame.Rect((0, 0), settings.PADDLE_SIZE)
        )
        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (settings.WIDTH / 2, settings.HEIGHT - 50)
        self.velocity = 10

    def left(self):
        self.rect.x -= self.velocity
        if self.rect.left <= 0:
            self.rect.left = 0

    def right(self):
        self.rect.x += self.velocity
        if self.rect.right >= settings.WIDTH:
            self.rect.right = settings.WIDTH

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.left()
        if keys[pygame.K_RIGHT]:
            self.right()


class Ball(pygame.sprite.Sprite):
    def __init__(self, game, speed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image = pygame.Surface(settings.BALL_SIZE)
        image.fill(settings.BLACK)
        image.set_colorkey(settings.BLACK)
        pygame.draw.circle(
            image,
            settings.WHITE,
            (settings.BALL_RADIUS, settings.BALL_RADIUS),
            settings.BALL_RADIUS,
        )
        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH / 2, settings.HEIGHT / 2)
        self.radius = settings.BALL_RADIUS
        self.velocity = pygame.Vector2(randint(-8, 8), speed)
        self.game = game

    def update(self):
        self.rect.centerx += self.velocity.x
        self.rect.centery += self.velocity.y
        if self.rect.left <= 0:
            self.rect.left = 0
            self.velocity.x *= -1
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity.y *= -1
        if self.rect.right >= settings.WIDTH:
            self.rect.right = settings.WIDTH
            self.velocity.x *= -1
        if self.rect.top >= settings.HEIGHT:
            self.kill()
            self.game.out()
        self.hit()

    def bounce(self):
        self.velocity.y *= -1
        self.velocity.x = randint(-8, 8)

    def hit(self):
        hits = pygame.sprite.spritecollide(
            self,
            self.game.sprites,
            False,
            pygame.sprite.collide_rect_ratio(0.85),
        )
        for sprite in hits:
            if isinstance(sprite, Paddle):
                self.game.sfx['bounce'].play()
                self.bounce()
            elif isinstance(sprite, Brick):
                sprite.kill()
                self.game.breakout(sprite)
                self.bounce()


class Status(pygame.sprite.Sprite):
    def __init__(self, spare_balls, score, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.reset_surface()
        self.font = pygame.font.Font(settings.FONT, 70)
        self.spare_balls = spare_balls
        self.score = score

    def reset_surface(self):
        image = pygame.Surface((settings.WIDTH, 100))
        image.fill(settings.BLACK)
        image.set_colorkey(settings.BLACK)
        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def update(self):
        self.reset_surface()
        self.draw_text(f'{self.spare_balls:>02}', settings.TEXT_LEFT)
        self.draw_text(f'{self.score:>03}', settings.TEXT_CENTER)

    def draw_text(self, text, position):
        surface = self.font.render(text, True, settings.WHITE)
        rect = surface.get_rect()
        rect.topleft = position
        self.image.blit(surface, rect)


class SplashScreen(pygame.sprite.Sprite):
    def __init__(self, text=settings.TITLE, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image = pygame.Surface(settings.WIN_SIZE)
        image.fill(settings.BLACK)
        image.set_colorkey(settings.BLACK)
        screen_center = (settings.WIDTH / 2, settings.HEIGHT / 2)
        font_big = pygame.font.Font(settings.FONT, 80)
        title = font_big.render(text, True, settings.WHITE)
        title_rect = title.get_rect()
        title_rect.midbottom = screen_center
        font_small = pygame.font.Font(settings.FONT, 30)
        hint = font_small.render('Press any key to play', True, settings.WHITE)
        hint_rect = hint.get_rect()
        hint_rect.midtop = screen_center
        image.blit(title, title_rect)
        image.blit(hint, hint_rect)
        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
