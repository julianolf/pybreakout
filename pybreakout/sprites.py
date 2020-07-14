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
