import pygame
import random
import config
from entities.entity import Entity
from typing import Optional # --- python 3.9.6 ---

class Bullet(Entity):
    def __init__(
        self,
        position: pygame.Vector2,
        target: Optional[pygame.Vector2] = None,
        speed: float = 300,
        damage: float = 0.1,
        color=(255, 255, 255),
        trail_length: int = 10,
        turn_rate: float = 0.0,
        effect=None,
    ):
        super().__init__(position, size=5, color=color)

        self.speed = speed
        self.damage = damage
        self.trail_length = trail_length
        self.turn_rate = turn_rate
        self.destroyed = False
        self.effect = effect
        self.direction = self._init_direction(target)

    def _init_direction(self, target: Optional[pygame.Vector2] = None) -> pygame.Vector2:
        if target is None:
            angle = random.uniform(0, 360)
            return pygame.Vector2(1, 0).rotate(angle)

        direction = target - self.position
        if direction.length_squared() == 0:
            return pygame.Vector2(1, 0)

        return direction.normalize()

    def update(self, dt: float, player):
        self.position += self.direction * self.speed * dt

        # kolizja z graczem
        if self.check_collision(player):
            self.on_hit(player)
            self.destroyed = True
            return

        if self._is_out_of_bounds():
            self.destroyed = True

    def _is_out_of_bounds(self) -> bool:
        margin = self.size
        return (
            self.position.x < -margin
            or self.position.x > config.BOARD_WIDTH + margin
            or self.position.y < -margin
            or self.position.y > config.BOARD_HEIGHT + margin
        )

    def on_hit(self, player):
        player.health -= self.damage
        if self.effect:
            player.add_effect(self.effect)
        self.destroyed = True
