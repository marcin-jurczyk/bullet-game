from __future__ import annotations
import pygame


class Entity:
    position: pygame.math.Vector2  # type hint for mypy
    def __init__(self, position, size, color):
        self.position = pygame.math.Vector2(position)
        self.size = size
        self.color = color
        self.destroyed = False

    def update(self, dt: float):
        pass

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(surface, self.color, self.position, self.size)

    def check_collision(self, other: Entity) -> bool:
        radius_sum = self.size + other.size
        return (
            self.position.distance_squared_to(other.position)
            <= radius_sum * radius_sum
    )

    def on_collision(self, other: Entity):
        pass
