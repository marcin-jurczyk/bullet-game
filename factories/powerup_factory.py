import random

import pygame
from entities.powerup.enlarge import EnlargePowerUp
from entities.powerup.shrink import ShrinkPowerUp
from entities.powerup.slow import SlowPowerUp
from entities.powerup.speed import SpeedPowerUp
from config import POWERUP_SIZE, BOARD_HEIGHT, BOARD_WIDTH


class PowerUpFactory:
    POWERUP_CLASSES = [SpeedPowerUp, SlowPowerUp, ShrinkPowerUp, EnlargePowerUp]

    @staticmethod
    def create_random(player=None, existing_powerups=None, max_attempts=1):
        cls = random.choice(PowerUpFactory.POWERUP_CLASSES)
        existing_powerups = existing_powerups or []

        for _ in range(max_attempts):
            position = pygame.Vector2(
                random.randint(POWERUP_SIZE, BOARD_WIDTH - POWERUP_SIZE),
                random.randint(POWERUP_SIZE, BOARD_HEIGHT - POWERUP_SIZE)
            )

            temp_entity = cls(position=position)

            collision = False
            if player and temp_entity.check_collision(player):
                collision = True
            else:
                for powerup in existing_powerups:
                    if temp_entity.check_collision(powerup):
                        collision = True
                        break

            if not collision:
                return temp_entity

        return cls(position=pygame.Vector2(POWERUP_SIZE, POWERUP_SIZE))

    @staticmethod
    def create_by_type(powerup_type, position=None):
        cls = next((c for c in PowerUpFactory.POWERUP_CLASSES if c.__name__ == powerup_type), None)
        if cls is None:
            raise ValueError(f"PowerUpFactory: unknown PowerUp type: {powerup_type}")

        if position is None:
            from config import BOARD_WIDTH, BOARD_HEIGHT
            position = pygame.Vector2(
                random.randint(POWERUP_SIZE, BOARD_WIDTH - (POWERUP_SIZE)),
                random.randint(POWERUP_SIZE, BOARD_HEIGHT - (POWERUP_SIZE))
            )

        return cls(position=position)
