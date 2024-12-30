from circleshape import CircleShape
from constants import SHOT_RADIUS
import pygame
from typing import override


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen: pygame.Surface):
        _ = pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt
