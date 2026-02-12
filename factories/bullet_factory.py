import random
import config
from pygame import Vector2
from entities.bullet.enlarge import EnlargeBullet
from entities.bullet.hard import HardBullet
from entities.bullet.light import LightBullet
from entities.bullet.normal import NormalBullet
from entities.bullet.slow import SlowBullet


class BulletFactory:
    BULLET_TYPES = [NormalBullet, SlowBullet, EnlargeBullet, HardBullet, LightBullet]

    @staticmethod
    def point_on_edge(edge, w, h):
        if edge == "top":
            return Vector2(random.uniform(0, w), 0)
        if edge == "bottom":
            return Vector2(random.uniform(0, w), h)
        if edge == "left":
            return Vector2(0, random.uniform(0, h))
        return Vector2(w, random.uniform(0, h))

    @staticmethod
    def target_outside_edge(edge, w, h, margin=50):
        if edge == "left":
            return Vector2(w + margin, random.uniform(0, h))
        if edge == "right":
            return Vector2(-margin, random.uniform(0, h))
        if edge == "top":
            return Vector2(random.uniform(0, w), h + margin)
        return Vector2(random.uniform(0, w), -margin)

    @staticmethod
    def random_edge_spawn():
        w, h = config.BOARD_WIDTH, config.BOARD_HEIGHT
        edge = random.choice(["top", "bottom", "left", "right"])
        pos = BulletFactory.point_on_edge(edge, w, h)
        return pos, edge

    @staticmethod
    def outside_target_for_edge(edge):
        w, h = config.BOARD_WIDTH, config.BOARD_HEIGHT
        return BulletFactory.target_outside_edge(edge, w, h, margin=50)

    @staticmethod
    def random_player_offset():
        r = config.PLAYER_OFFSET_RANGE
        return Vector2(random.uniform(-r, r), random.uniform(-r, r))

    @classmethod
    def create(cls, player_position: Vector2):
        bullet_cls = random.choice(cls.BULLET_TYPES)
        position, edge = cls.random_edge_spawn()

        if random.random() < config.BULLET_TARGET_PLAYER_CHANCE:
            # Immediate homing
            initial_target = player_position + cls.random_player_offset()
            bullet = bullet_cls(position, initial_target)
            bullet.movement.focus_on(player_position)
        else:
            # Delayed homing
            initial_target = cls.outside_target_for_edge(edge)
            bullet = bullet_cls(position, initial_target)
            bullet.movement.focus_on(player_position)

        return bullet

