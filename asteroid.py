from typing import override
import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface):
        _ = pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # If the asteroid was the smallest kind, do nothing.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:  # Otherwise, spawn two smaller ones.
            ran_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(ran_angle)
            vel2 = self.velocity.rotate(-ran_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

            new_ast_1.velocity = vel1 * 1.2
            new_ast_2.velocity = vel2 * 1.2
