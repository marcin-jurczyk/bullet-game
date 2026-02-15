# factories/point_factory.py

import random
from typing import Optional
from pygame import Vector2
import config
from entities.point import Point


class PointFactory:

    @staticmethod
    def random_spawn_position() -> Vector2:
        return Vector2(
            random.uniform(0, config.BOARD_WIDTH),
            random.uniform(0, config.BOARD_HEIGHT)
        )

    @staticmethod
    def random_color():
        return random.choice(config.POINT_COLORS)

    @staticmethod
    def random_value() -> int:
        return random.choice([1, 2, 5])

    @classmethod
    def create(cls, existing_points: list[Point]) -> Optional[Point]:
        if len(existing_points) >= config.MAX_POINTS_ON_BOARD:
            return None

        return Point(
            position=cls.random_spawn_position(),
            color=cls.random_color(),
            value=cls.random_value()
        )
