import pygame
from config import SHIELD_RADIUS_OFFSET
from entities.bullet.bullet_movement import BulletMovement
from entities.entity import Entity


class Bullet(Entity):
    def __init__(
        self,
        position: pygame.Vector2,
        movement: BulletMovement,
        damage: float,
        size: float,
        color,
        effect=None,
    ):
        super().__init__(position, size=size, color=color)
        self.movement = movement
        self.damage = damage
        self.effect = effect

    def update(self, dt: float, player):
        self.movement.update(self, dt)

        if self.check_shield_collision(player):
            self.destroyed = True
            return

        if self.check_collision(player):
            self.on_hit(player)
            return

        if self.is_out_of_bounds():
            self.destroyed = True

    def on_hit(self, player):
        player.health -= self.damage
        if self.effect:
            player.add_effect(self.effect)
        self.destroyed = True

    def check_shield_collision(self, player) -> bool:
        if not player.has_shield:
            return False

        distance = self.position.distance_to(player.position)
        shield_radius = player.size + SHIELD_RADIUS_OFFSET + self.size

        return distance <= shield_radius

