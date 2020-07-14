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
