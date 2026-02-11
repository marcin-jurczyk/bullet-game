from typing import Optional
import pygame


class BulletMovement:
    def __init__(
        self,
        position: pygame.Vector2,
        speed: float,
        target_position: Optional[pygame.Vector2] = None,
        turn_rate: float = 0.0
    ):
        self.direction = self._compute_initial_direction(position, target_position)
        self.speed = speed
        self.turn_rate = turn_rate
        self.target: Optional[pygame.Vector2] = None

    @staticmethod
    def _compute_initial_direction(
        position: pygame.Vector2,
        target_position: Optional[pygame.Vector2]
    ) -> pygame.Vector2:
        if target_position:
            delta = target_position - position
            if delta.length_squared() > 0:
                return delta.normalize()

        return pygame.Vector2(1, 0)

    def focus_on(self, target: pygame.Vector2):
        self.target = target

    def clear_target(self):
        self.target = None

    def update(self, bullet, dt: float):
        if self.target:
            self._update_homing(bullet.position, dt)

        bullet.position += self.direction * self.speed * dt

    def _update_homing(self, position: pygame.Vector2, dt: float):
        if self.target is None:
            return

        desired = self.target - position
        if desired.length_squared() == 0:
            return

        t = min(1.0, self.turn_rate * dt)
        self.direction = self.direction.lerp(
            desired.normalize(), t
        ).normalize()
