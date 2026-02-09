import random
import pygame
import config

from entities.bullet.normal import NormalBullet


class BulletFactory:
    BULLET_TYPES = [
        NormalBullet
    ]

    @staticmethod
    def random_edge_spawn():
        w, h = config.BOARD_WIDTH, config.BOARD_HEIGHT
        edge = random.choice(["top", "bottom", "left", "right"])

        if edge == "top":
            return pygame.Vector2(random.uniform(0, w), 0), "top"
        if edge == "bottom":
            return pygame.Vector2(random.uniform(0, w), h), "bottom"
        if edge == "left":
            return pygame.Vector2(0, random.uniform(0, h)), "left"
        return pygame.Vector2(w, random.uniform(0, h)), "right"

    @staticmethod
    def random_outside_target(edge: str) -> pygame.Vector2:
        w, h = config.BOARD_WIDTH, config.BOARD_HEIGHT
        margin = 50  # ensures bullet exits fully

        if edge == "left":
            return pygame.Vector2(w + margin, random.uniform(0, h))
        if edge == "right":
            return pygame.Vector2(-margin, random.uniform(0, h))
        if edge == "top":
            return pygame.Vector2(random.uniform(0, w), h + margin)
        return pygame.Vector2(random.uniform(0, w), -margin)

    @staticmethod
    def random_player_offset() -> pygame.Vector2:
        return pygame.Vector2(
            random.uniform(-config.PLAYER_OFFSET_RANGE, config.PLAYER_OFFSET_RANGE),
            random.uniform(-config.PLAYER_OFFSET_RANGE, config.PLAYER_OFFSET_RANGE),
        )

    @classmethod
    def create(cls, player_position: pygame.Vector2):
        bullet_cls = random.choice(cls.BULLET_TYPES)
        position, edge = cls.random_edge_spawn()

        if random.random() < config.BULLET_TARGET_PLAYER_CHANCE:
            target = player_position + cls.random_player_offset()
        else:
            target = cls.random_outside_target(edge)

        return bullet_cls(position=position, target=target)

