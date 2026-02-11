import pygame
import config
from effects.slow import SlowEffect
from entities.bullet.bullet import Bullet
from entities.bullet.bullet_movement import BulletMovement


class SlowBullet(Bullet):
    def __init__(
        self,
        position: pygame.Vector2,
        initial_target: pygame.Vector2,
    ):
        movement = BulletMovement(
            position=position,
            speed=config.SLOW_BULLET_SPEED,
            target_position=initial_target,
            turn_rate=config.BULLET_TURN_RATE,
        )

        super().__init__(
            position=position,
            movement=movement,
            damage=config.SLOW_BULLET_DAMAGE,
            size=config.SLOW_BULLET_SIZE,
            color=config.SLOW_BULLET_COLOR,
            effect=SlowEffect()
        )

