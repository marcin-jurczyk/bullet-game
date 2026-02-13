import pygame
from effects.base import Effect
from config import SHIELD_POWERUP_TIME, SHIELD_RADIUS_OFFSET


class ShieldEffect(Effect):
    key = "shield"

    def __init__(self, duration: float = SHIELD_POWERUP_TIME):
        super().__init__(duration, 0)

    def on_apply(self, player):
        player.has_shield = True

    def on_update(self, player, dt: float):
        pass

    def on_expire(self, player):
        player.has_shield = False

    def draw(self, surface, player):
        if not surface:
            return

        pygame.draw.circle(
            surface,
            (0, 160, 255),
            player.position,
            player.size + SHIELD_RADIUS_OFFSET,
            width=2
        )