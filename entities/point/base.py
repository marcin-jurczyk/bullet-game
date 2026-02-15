# entities/point/point.py

import pygame
import config
from entities.entity import Entity
from entities.player.base import Player


class Point(Entity):
    def __init__(self, position: pygame.Vector2, color, value: int):
        super().__init__(position=position, size=config.POINT_SIZE, color=color)

        self.value = value
        self.remaining_time = config.POINT_LIFETIME

    def update(self, dt: float):
        self.remaining_time -= dt
        if self.remaining_time <= 0:
            self.destroyed = True

    def on_collision(self, other):
        receiver = getattr(other, "receive_points", None)
        if callable(receiver):
            receiver(self.value)
            self.destroyed = True