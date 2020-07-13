import pygame

from . import settings


class Wall(pygame.sprite.Sprite):
    def __init__(self, size, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image = pygame.Surface(size)
        image.fill(settings.BLACK)
        image.set_colorkey(settings.BLACK)
        pygame.draw.rect(image, settings.WHITE, pygame.Rect((0, 0), size))
        self.image = image.convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = position


class TopWall(Wall):
    def __init__(self, *args, **kwargs):
        size = (settings.WIDTH, 20)
        position = (0, 60)
        super().__init__(size, position, *args, **kwargs)


class LeftWall(Wall):
    def __init__(self, *args, **kwargs):
        size = (10, settings.HEIGHT)
        position = (0, 0)
        super().__init__(size, position, *args, **kwargs)


class RightWall(Wall):
    def __init__(self, *args, **kwargs):
        size = (10, settings.HEIGHT)
        position = (settings.WIDTH - 10, 0)
        super().__init__(size, position, *args, **kwargs)
