from entities.bullet.bullet import Bullet
import config

class NormalBullet(Bullet):
    def __init__(self, position, target=None):
        super().__init__(
            position=position,
            target=target,
            speed=config.NORMAL_BULLET_SPEED,
            damage=config.NORMAL_BULLET_DAMAGE,
            color=config.NORMAL_BULLET_COLOR,
            trail_length=config.NORMAL_BULLET_TRAIL_LENGTH,
            turn_rate=config.BULLET_TURN_RATE_DEFAULT,
            effect=None
        )
        self.size = config.NORMAL_BULLET_SIZE