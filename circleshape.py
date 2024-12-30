import pygame
from pygame.math import Vector2

# Base class for game objects


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: Vector2 = pygame.Vector2(x, y)
        self.velocity: Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass
